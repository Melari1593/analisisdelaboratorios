import test from 'node:test';
import assert from 'node:assert/strict';
import { createApp } from './server.mjs';

async function withServer(fn, fetcher = async (_url, options) => {
  const request = JSON.parse(options.body);
  assert.equal(request.store, false);
  assert.equal(request.input[0].content[1].type, 'input_file');
  return { ok: true, json: async () => ({ output: [{ content: [{ type: 'output_text', text: JSON.stringify({ resumen:'Lectura',hallazgos:[],preguntas:[],limitaciones:[],atencion:'Consultar.' }) }] }] }) };
}) {
  const server = createApp({ apiKey: 'test', accessToken: 'secret', fetcher });
  await new Promise(resolve => server.listen(0, '127.0.0.1', resolve));
  try { await fn(`http://127.0.0.1:${server.address().port}`); } finally { await new Promise(resolve => server.close(resolve)); }
}
const sample = { name: 'informe.pdf', type: 'application/pdf', data: 'data:application/pdf;base64,'+Buffer.from('%PDF-1.4\n%%EOF').toString('base64') };
const send = (url, files, token = 'secret') => fetch(url+'/api/interpret', { method:'POST', headers:{'Content-Type':'application/json',Authorization:`Bearer ${token}`}, body:JSON.stringify({ kind:'laboratorio',context:'',files }) });
test('auth and valid PDF request with no provider storage', async () => withServer(async url => {
  assert.equal((await send(url,[sample],'wrong')).status,401);
  const r=await send(url,[sample]);assert.equal(r.status,200);assert.equal((await r.json()).result.resumen,'Lectura');
}));
test('rejects disguised document before calling provider', async () => withServer(async url => {
  const r=await send(url,[{...sample,data:'data:application/pdf;base64,'+Buffer.from('NOT A PDF').toString('base64')}]);
  assert.equal(r.status,400);
}));

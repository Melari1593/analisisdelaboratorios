(function(){
"use strict";
const $ = (s, r=document) => r.querySelector(s);
const el = (tag, attrs={}, ...kids) => {
  const n = document.createElement(tag);
  for (const [k,v] of Object.entries(attrs)) {
    if (k === "class") n.className = v;
    else if (k === "text") n.textContent = v;
    else if (k.startsWith("on")) n.addEventListener(k.slice(2), v);
    else if (v !== false && v != null) n.setAttribute(k, v === true ? "" : v);
  }
  for (const k of kids) if (k != null) n.append(k);
  return n;
};
const norm = s => String(s).normalize("NFD").replace(/[̀-ͯ]/g,"").toLowerCase();
const barajar = a => { for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(Math.random()*(i+1)); [a[i],a[j]] = [a[j],a[i]]; } return a; };

/* ---------- Almacenamiento local (solo en este navegador) ---------- */
const store = {
  get(k, d){ try { const v = localStorage.getItem(k); return v ? JSON.parse(v) : d; } catch { return d; } },
  set(k, v){ try { localStorage.setItem(k, JSON.stringify(v)); } catch {} }
};

/* ---------- Markdown mínimo (sin dependencias) ---------- */
const escHTML = s => s.replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;");
function inline(s){
  const codes = [];
  s = escHTML(s).replace(/`([^`]+)`/g, (_, c) => { codes.push(c); return "\u0000" + (codes.length - 1) + "\u0000"; });
  s = s.replace(/\*\*(.+?)\*\*/g, "<strong>$1</strong>")
       .replace(/(^|[^*\w])\*(?!\s)([^*\n]+?)\*(?!\w)/g, "$1<em>$2</em>");
  return s.replace(/\u0000(\d+)\u0000/g, (_, i) => "<code>" + codes[i] + "</code>");
}
function md2html(md){
  const L = md.replace(/\r/g,"").split("\n");
  let out = "", para = [], i = 0;
  const flush = () => { if (para.length) { out += "<p>" + inline(para.join(" ")) + "</p>"; para = []; } };
  const esTabla = k => /^\s*\|/.test(L[k] || "") && /^\s*\|?\s*:?-{2,}/.test(L[k+1] || "");
  const celdas = l => l.trim().replace(/^\|/,"").replace(/\|$/,"").split("|").map(c => c.trim());
  const itemRe = /^(\s*)([-*+]|\d+[.)])\s+(.*)$/;
  while (i < L.length) {
    const l = L[i];
    if (!l.trim()) { flush(); i++; continue; }
    let m;
    if ((m = l.match(/^(#{1,6})\s+(.*)$/))) { flush(); const n = m[1].length; out += `<h${n}>${inline(m[2])}</h${n}>`; i++; continue; }
    if (/^\s*(-{3,}|\*{3,})\s*$/.test(l)) { flush(); out += "<hr>"; i++; continue; }
    if (esTabla(i)) {
      flush();
      const head = celdas(L[i]); i += 2;
      let t = "<table><thead><tr>" + head.map(c => "<th>" + inline(c) + "</th>").join("") + "</tr></thead><tbody>";
      while (i < L.length && /^\s*\|/.test(L[i])) { t += "<tr>" + celdas(L[i]).map(c => "<td>" + inline(c) + "</td>").join("") + "</tr>"; i++; }
      out += t + "</tbody></table>"; continue;
    }
    if (/^\s*>/.test(l)) {
      flush(); const q = [];
      while (i < L.length && /^\s*>/.test(L[i])) { q.push(L[i].replace(/^\s*>\s?/,"")); i++; }
      out += "<blockquote>" + md2html(q.join("\n")) + "</blockquote>"; continue;
    }
    if (itemRe.test(l)) {
      flush();
      const stack = [];
      let buf = null;
      const volcar = () => { if (buf != null) { out += inline(buf); buf = null; } };
      const cerrar = hasta => { volcar(); while (stack.length > hasta) { const s = stack.pop(); out += "</li></" + s.tipo + ">"; } };
      while (i < L.length) {
        const x = L[i];
        if (!x.trim()) { if (itemRe.test(L[i+1] || "") || /^\s{2,}\S/.test(L[i+1] || "")) { i++; continue; } break; }
        const mm = x.match(itemRe);
        if (mm) {
          volcar();
          const ind = mm[1].replace(/\t/g,"  ").length, tipo = /\d/.test(mm[2]) ? "ol" : "ul";
          while (stack.length && ind < stack[stack.length-1].ind) cerrar(stack.length - 1);
          let top = stack[stack.length-1];
          if (top && ind === top.ind && tipo !== top.tipo) { cerrar(stack.length - 1); top = stack[stack.length-1]; }
          if (!top || ind > top.ind) { stack.push({ ind, tipo }); out += "<" + tipo + "><li>"; }
          else out += "</li><li>";
          buf = mm[3]; i++;
        } else if (/^\s+\S/.test(x) && stack.length) { buf = (buf ?? "") + " " + x.trim(); i++; }
        else break;
      }
      cerrar(0); continue;
    }
    para.push(l.trim()); i++;
  }
  flush();
  return out;
}

/* ---------- Datos: incrustados (versión autocontenida) o por red (desarrollo) ---------- */
const ARCHIVOS = [
  { f:"estrategia-examen.md", grupo:"Examen", unico:"Estrategia, MBE y expediente" },
  { f:"ciencias-basicas.md", grupo:"Ciencias básicas" },
  { f:"neurologia-cardiologia.md", grupo:"Clínica" },
  { f:"neumologia-gastro.md", grupo:"Clínica" },
  { f:"endocrino-hemato-dermato.md", grupo:"Clínica" },
  { f:"nefro-urologia-ginecologia.md", grupo:"Clínica" },
  { f:"obstetricia-reumatologia.md", grupo:"Clínica" },
  { f:"psiquiatria-orl-geriatria-trauma.md", grupo:"Clínica" }
];
const BANCOS = ["estrategia","ciencias-basicas","neurologia-cardiologia","cardiologia-base","neumologia-gastro",
  "endocrino-hemato-dermato","nefro-urologia-ginecologia","obstetricia-reumatologia","psiquiatria-orl-geriatria-trauma"];

async function obtenerDatos(){
  const emb = document.getElementById("enarm-data");
  if (emb && emb.textContent.trim()) return JSON.parse(emb.textContent);
  const apuntes = {};
  await Promise.all(ARCHIVOS.map(a => fetch("apuntes/" + a.f).then(r => { if (!r.ok) throw new Error(a.f); return r.text(); }).then(t => apuntes[a.f] = t)));
  const banco = [];
  await Promise.all(BANCOS.map(b => fetch("banco/" + b + ".json").then(r => r.ok ? r.json() : []).catch(() => []).then(arr => {
    arr.forEach((q,k) => banco.push({ ...q, id: q.id || `${b}-${k+1}` }));
  })));
  return { apuntes, banco };
}

/* ---------- Pestañas ---------- */
const tabs = [...document.querySelectorAll("nav.tabs button")];
function show(view){
  for (const b of tabs) {
    const on = b.dataset.view === view;
    b.setAttribute("aria-selected", on);
    $("#view-" + b.dataset.view).hidden = !on;
  }
  if (view === "progreso") renderProgreso();
  if (view === "simulacro") disponibles();
  store.set("enarm.tab", view);
}
tabs.forEach(b => b.addEventListener("click", () => show(b.dataset.view)));

/* ---------- Apuntes ---------- */
let SPECS = [], BANCO = [];

function partir(md, nivel){
  const re = nivel === 2 ? /^## (.+)$/gm : /^### (.+)$/gm;
  const idx = []; let m;
  while ((m = re.exec(md))) idx.push({ t:m[1].trim(), i:m.index });
  return idx.map((h,k) => ({ titulo:h.t, md: md.slice(h.i, k+1 < idx.length ? idx[k+1].i : md.length) }));
}
const limpiar = t => t.replace(/^\d+\.\s*/,"").replace(/\s*\(.*\)\s*$/,"").trim();
const plano = t => t.replace(/[*_`]/g,"");

function construir(apuntes){
  for (const a of ARCHIVOS) {
    const md = (apuntes[a.f] || "").replace(/^# .*\n/, "");
    if (a.unico) {
      SPECS.push({ id:"estrategia", label:a.unico, grupo:a.grupo, md, nivelTema:2, topics: partir(md,2) });
      continue;
    }
    for (const s of partir(md,2)) {
      const label = limpiar(s.titulo);
      const topics = partir(s.md,3);
      SPECS.push({ id: norm(label).replace(/[^a-z0-9]+/g,"-"), label, grupo:a.grupo, md:s.md, nivelTema:3,
        topics: topics.length ? topics : [{ titulo:s.titulo, md:s.md }] });
    }
  }
}
const specDe = label => SPECS.find(s => s.label === label);
function temaIdx(spec, tema){
  if (!spec || !tema) return -1;
  const t = norm(plano(tema));
  let k = spec.topics.findIndex(x => norm(plano(x.titulo)) === t);
  if (k < 0) k = spec.topics.findIndex(x => { const a = norm(plano(x.titulo)); return a.startsWith(t) || t.startsWith(a.split(" (")[0]); });
  return k;
}

function renderTOC(){
  const toc = $("#toc"); toc.textContent = "";
  for (const g of [...new Set(SPECS.map(s => s.grupo))]) {
    const ul = el("ul");
    for (const s of SPECS.filter(x => x.grupo === g))
      ul.append(el("li", {}, el("button", { "data-id":s.id, text:s.label, onclick:() => abrir(s.id) })));
    toc.append(el("div", {}, el("h4", { class:"eyebrow", text:g }), ul));
  }
}

function abrir(id, k){
  const s = SPECS.find(x => x.id === id); if (!s) return;
  document.querySelectorAll("#toc button").forEach(b => b.setAttribute("aria-current", b.dataset.id === id));
  const doc = $("#doc");
  doc.innerHTML = md2html(s.md);
  doc.querySelectorAll("table").forEach(t => { const w = el("div", { class:"tbl" }); t.replaceWith(w); w.append(t); });
  doc.querySelectorAll("li, p").forEach(n => { if (n.textContent.includes("⚠️")) n.classList.add("upd"); });
  [...doc.querySelectorAll(s.nivelTema === 2 ? "h2" : "h3")].forEach((h,j) => h.id = "t-" + j);
  const tp = $("#topics"); tp.textContent = "";
  s.topics.forEach((t,j) => tp.append(el("button", { text:plano(t.titulo), onclick:() => $("#t-" + j)?.scrollIntoView({ behavior:"smooth" }) })));
  store.set("enarm.spec", id);
  if (k != null && k >= 0) requestAnimationFrame(() => $("#t-" + k)?.scrollIntoView());
  else window.scrollTo({ top:0 });
}

$("#q").addEventListener("input", e => {
  const q = norm(e.target.value.trim());
  const hits = $("#hits"), toc = $("#toc");
  if (q.length < 3) { hits.hidden = true; toc.hidden = false; return; }
  hits.textContent = "";
  let n = 0;
  outer: for (const s of SPECS) {
    for (let k = 0; k < s.topics.length; k++) {
      const t = s.topics[k]; const txt = t.md.replace(/[#*|`>_]+/g," ").replace(/\s+/g," ");
      const i = norm(txt).indexOf(q);
      if (i < 0) continue;
      const a = Math.max(0, i - 50), frag = txt.slice(a, i + q.length + 70);
      const j = norm(frag).indexOf(q);
      const small = el("small");
      small.append((a ? "…" : "") + frag.slice(0,j), el("mark", { text:frag.slice(j, j+q.length) }), frag.slice(j+q.length) + "…");
      hits.append(el("button", { class:"hit", onclick:() => abrir(s.id, k) }, el("b", { text:plano(t.titulo) }), el("small", { text:s.label }), small));
      if (++n >= 40) break outer;
    }
  }
  if (!n) hits.append(el("p", { class:"note", text:"Sin resultados en los apuntes." }));
  hits.hidden = false; toc.hidden = true;
});

/* ---------- Simulacro ---------- */
const stats = () => store.get("enarm.preg", {});

function llenarSelects(){
  const sel = $("#s-esp"); sel.textContent = "";
  sel.append(el("option", { value:"", text:"Todas las especialidades (mixto)" }));
  for (const s of SPECS) {
    const n = BANCO.filter(q => q.especialidad === s.label).length;
    if (n) sel.append(el("option", { value:s.label, text:`${s.label} (${n})` }));
  }
  const prev = store.get("enarm.simEsp", "Cardiovascular");
  if ([...sel.options].some(o => o.value === prev)) sel.value = prev;
  llenarTemas();
}
function llenarTemas(){
  const esp = $("#s-esp").value, sel = $("#s-tema"); sel.textContent = "";
  sel.append(el("option", { value:"", text:"Todos los temas" }));
  if (esp) {
    const temas = [...new Set(BANCO.filter(q => q.especialidad === esp).map(q => q.tema).filter(Boolean))].sort((a,b) => a.localeCompare(b, "es"));
    for (const t of temas) sel.append(el("option", { value:t, text:plano(t) }));
  }
  sel.disabled = !esp;
  disponibles();
}
$("#s-esp").addEventListener("change", () => { llenarTemas(); store.set("enarm.simEsp", $("#s-esp").value); });
$("#s-tema").addEventListener("change", disponibles);
$("#s-modo").addEventListener("change", disponibles);

function candidatos(){
  const esp = $("#s-esp").value, tema = $("#s-tema").value, modo = $("#s-modo").value, st = stats();
  let pool = BANCO.filter(q => (!esp || q.especialidad === esp) && (!tema || q.tema === tema));
  const vistos = pool.filter(q => st[q.id]), nuevos = pool.filter(q => !st[q.id]);
  const fallados = pool.filter(q => st[q.id] && st[q.id].ult === false);
  if (modo === "errores") return { lista: barajar(fallados), pool, nuevos, fallados };
  if (modo === "nuevos") {
    const viejos = barajar(vistos).sort((a,b) => (st[a.id].ult ? 1 : 0) - (st[b.id].ult ? 1 : 0));
    return { lista: [...barajar(nuevos), ...viejos], pool, nuevos, fallados };
  }
  return { lista: barajar([...pool]), pool, nuevos, fallados };
}
function disponibles(){
  if (!BANCO.length) return;
  const { lista, pool, nuevos, fallados } = candidatos();
  $("#s-disp").textContent = `${pool.length} reactivos · ${nuevos.length} sin ver · ${fallados.length} fallados la última vez`;
  $("#empezar").disabled = !lista.length;
  $("#s-status").textContent = !lista.length && $("#s-modo").value === "errores" ? "No tienes reactivos fallados con este filtro." : "";
}

$("#empezar").addEventListener("click", () => {
  const n = Number($("#s-n").value);
  const { lista } = candidatos();
  if (!lista.length) return;
  const esp = $("#s-esp").value || "Mixto";
  iniciar(lista.slice(0, n), esp);
});

let Q = null;
function iniciar(preguntas, esp){
  Q = { preguntas, esp, i:0, resp:[] };
  $("#setup").hidden = true;
  pintarPregunta();
  window.scrollTo({ top:0 });
}

function pintarPregunta(){
  const box = $("#quiz"); box.textContent = "";
  const q = Q.preguntas[Q.i], total = Q.preguntas.length;
  box.append(
    el("div", { class:"qhead" },
      el("span", { class:"eyebrow", text:`Reactivo ${Q.i + 1} de ${total} · ${q.especialidad}` }),
      el("button", { class:"btn", text:"Terminar aquí", onclick:() => Q.resp.length ? terminar() : salir() })),
    el("div", { class:"progressbar" }, el("i", { style:`width:${(Q.i / total) * 100}%` })));
  const opts = el("div", { class:"opts" });
  const expl = el("div", { class:"expl", hidden:true });
  for (const l of ["A","B","C","D"])
    opts.append(el("button", { class:"opt", "data-l":l, onclick:() => responder(l, opts, expl) },
      el("span", { class:"l", text:l }), el("span", { text:q.opciones[l] })));
  box.append(el("div", { class:"qcard" },
    q.tema ? el("div", {}, el("span", { class:"chip", text:plano(q.tema) })) : null,
    el("p", { class:"caso", text:q.caso }),
    el("p", { class:"preg", text:q.pregunta }),
    opts, expl));
}

function responder(l, opts, expl){
  const q = Q.preguntas[Q.i], ok = l === q.correcta;
  Q.resp[Q.i] = l;
  const st = stats(), s = st[q.id] || { v:0, a:0 };
  s.v++; if (ok) s.a++; s.ult = ok; s.t = Date.now(); st[q.id] = s; store.set("enarm.preg", st);
  opts.querySelectorAll(".opt").forEach(b => {
    b.disabled = true;
    if (b.dataset.l === q.correcta) b.classList.add("ok");
    else if (b.dataset.l === l) b.classList.add("bad");
  });
  const ul = el("ul");
  for (const k of ["A","B","C","D"]) {
    if (k === q.correcta || !q.distractores?.[k]) continue;
    ul.append(el("li", {}, el("b", { text:`${k}) ` }), q.distractores[k]));
  }
  const spec = specDe(q.especialidad), k = temaIdx(spec, q.tema);
  const ultimo = Q.i === Q.preguntas.length - 1;
  expl.append(
    el("div", { class:"verdict " + (ok ? "ok" : "bad"), text: ok ? "Correcto" : `Incorrecto. La respuesta es ${q.correcta}.` }),
    el("p", { style:"margin:0", text:q.explicacion || "" }),
    ul.children.length ? el("div", {}, el("div", { class:"eyebrow", text:"Por qué no las otras" }), ul) : null,
    q.perla ? el("div", { class:"perla" }, el("b", { text:"Perla: " }), q.perla) : null,
    el("div", { class:"actions", style:"display:flex;flex-wrap:wrap;gap:10px" },
      el("button", { class:"btn primary", text: ultimo ? "Ver resultado" : "Siguiente reactivo",
        onclick:() => { if (ultimo) terminar(); else { Q.i++; pintarPregunta(); window.scrollTo({ top:0 }); } } }),
      spec ? el("button", { class:"btn", text:"Ver el tema en los apuntes", onclick:() => { show("estudiar"); abrir(spec.id, k); } }) : null));
  expl.hidden = false;
  expl.querySelector(".btn.primary").focus({ preventScroll:true });
}

function terminar(){
  const hechos = Q.preguntas.slice(0, Q.resp.length);
  const total = hechos.length;
  const aciertos = hechos.filter((q,i) => Q.resp[i] === q.correcta).length;
  const hist = store.get("enarm.historial", []);
  hist.push({ t:Date.now(), esp:Q.esp, ok:aciertos, n:total });
  store.set("enarm.historial", hist.slice(-300));

  const box = $("#quiz"); box.textContent = "";
  const lista = el("ul", { class:"review" });
  hechos.forEach((q,i) => {
    const ok = Q.resp[i] === q.correcta;
    lista.append(el("li", {},
      el("span", { class:"mk " + (ok ? "ok" : "bad"), text: ok ? "✓" : "✗" }),
      el("span", { text:`${i + 1}. ${plano(q.tema || q.pregunta)}` }),
      el("span", { class:"note", text: ok ? q.correcta : `${Q.resp[i]} → ${q.correcta}` })));
  });
  const repaso = el("div", { class:"topics" });
  const vistos = new Set();
  hechos.forEach((q,i) => {
    if (Q.resp[i] === q.correcta || !q.tema || vistos.has(q.tema)) return;
    vistos.add(q.tema);
    const spec = specDe(q.especialidad), k = temaIdx(spec, q.tema);
    if (spec) repaso.append(el("button", { text:plano(q.tema), onclick:() => { show("estudiar"); abrir(spec.id, k); } }));
  });
  box.append(el("div", { class:"summary" },
    el("div", { class:"score" }, el("b", { text:`${aciertos}/${total}` }), el("span", { class:"muted", text:`${total ? Math.round(aciertos / total * 100) : 0} % · ${Q.esp}` })),
    lista,
    repaso.children.length ? el("div", {}, el("div", { class:"eyebrow", text:"Repasa estos temas" }), repaso)
      : el("p", { class:"muted", text:"Sin errores. Vuelve a probarte en unos días para confirmar que lo recuerdas." }),
    el("div", { style:"display:flex;flex-wrap:wrap;gap:10px" },
      el("button", { class:"btn primary", text:"Otro simulacro", onclick: salir }),
      el("button", { class:"btn", text:"Ver mi progreso", onclick:() => show("progreso") }))));
  window.scrollTo({ top:0 });
}
function salir(){ Q = null; $("#quiz").textContent = ""; $("#setup").hidden = false; disponibles(); }

/* ---------- Calculadora ---------- */
const num = id => { const v = parseFloat($(id).value); return isFinite(v) && v >= 0 ? v : 0; };
const pc = x => isFinite(x) ? (x * 100).toFixed(1) + " %" : "—";
const fx = (x, d=2) => isFinite(x) ? x.toFixed(d) : "—";
function filas(dl, rows){
  dl.textContent = "";
  for (const [nombre, formula, valor] of rows)
    dl.append(el("div", {}, el("dt", {}, nombre, el("small", { text:formula })), el("dd", { text:valor })));
}
function calcular(){
  const a = num("#d-a"), b = num("#d-b"), c = num("#d-c"), d = num("#d-d"), N = a+b+c+d;
  const S = a/(a+c), E = d/(b+d), LRp = S/(1-E), LRn = (1-S)/E;
  filas($("#d-res"), [
    ["Sensibilidad", `a/(a+c) = ${a}/${a+c}`, pc(S)],
    ["Especificidad", `d/(b+d) = ${d}/${b+d}`, pc(E)],
    ["Valor predictivo positivo", `a/(a+b) = ${a}/${a+b}`, pc(a/(a+b))],
    ["Valor predictivo negativo", `d/(c+d) = ${d}/${c+d}`, pc(d/(c+d))],
    ["Razón de verosimilitud +", "S/(1−E)", fx(LRp)],
    ["Razón de verosimilitud −", "(1−S)/E", fx(LRn, 3)],
    ["Prevalencia en la tabla", `(a+c)/N = ${a+c}/${N}`, pc((a+c)/N)]
  ]);
  const P = Math.min(Math.max(num("#d-pre") / 100, 0), 0.9999), mo = P/(1-P);
  const post = lr => { const m = mo*lr; return m/(1+m); };
  filas($("#d-post"), [
    ["Si la prueba sale positiva", `momios ${fx(mo)} × RV+ ${fx(LRp)}`, pc(post(LRp))],
    ["Si la prueba sale negativa", `momios ${fx(mo)} × RV− ${fx(LRn,3)}`, pc(post(LRn))]
  ]);
  const EC = num("#t-ec")/100, EE = num("#t-ee")/100, RR = EE/EC, dif = EC - EE;
  filas($("#t-res"), dif >= 0 ? [
    ["Riesgo relativo", `EE/EC = ${fx(EE,3)}/${fx(EC,3)}`, fx(RR)],
    ["Reducción del riesgo relativo", "1 − RR", pc(1-RR)],
    ["Reducción del riesgo absoluto", "EC − EE", pc(dif)],
    ["Número necesario a tratar", "1/RRA, redondeado hacia arriba", dif > 0 ? String(Math.ceil(1/dif)) : "—"]
  ] : [
    ["Riesgo relativo", `EE/EC = ${fx(EE,3)}/${fx(EC,3)}`, fx(RR)],
    ["Incremento del riesgo absoluto", "EE − EC", pc(-dif)],
    ["Número necesario para dañar", "1/IRA, redondeado hacia arriba", String(Math.ceil(1/(-dif)))]
  ]);
  const ca = num("#c-a"), cb = num("#c-b"), cc = num("#c-c"), cd = num("#c-d");
  filas($("#c-res"), [
    ["Riesgo en expuestos", `a/(a+b) = ${ca}/${ca+cb}`, pc(ca/(ca+cb))],
    ["Riesgo en no expuestos", `c/(c+d) = ${cc}/${cc+cd}`, pc(cc/(cc+cd))],
    ["Riesgo relativo (cohorte)", "[a/(a+b)] / [c/(c+d)]", fx((ca/(ca+cb))/(cc/(cc+cd)))],
    ["Razón de momios (casos y controles)", "(a×d)/(b×c)", fx((ca*cd)/(cb*cc))],
    ["Riesgo atribuible", "a/(a+b) − c/(c+d)", pc(ca/(ca+cb) - cc/(cc+cd))]
  ]);
}
document.querySelectorAll("#view-calculadora input").forEach(i => i.addEventListener("input", calcular));

/* ---------- Progreso ---------- */
function renderProgreso(){
  const box = $("#prog"); box.textContent = "";
  const st = stats();
  const vistos = BANCO.filter(q => st[q.id]);
  if (!vistos.length) {
    box.append(el("div", { class:"empty" },
      el("p", { style:"margin:0 0 10px", text:`Aún no has respondido reactivos en este navegador. El banco tiene ${BANCO.length}.` }),
      el("button", { class:"btn primary", text:"Hacer mi primer simulacro", onclick:() => show("simulacro") })));
    return;
  }
  const por = {};
  for (const q of BANCO) {
    const p = por[q.especialidad] ||= { total:0, vistos:0, v:0, a:0, fall:0 };
    p.total++;
    const s = st[q.id]; if (!s) continue;
    p.vistos++; p.v += s.v; p.a += s.a; if (s.ult === false) p.fall++;
  }
  const tbody = el("tbody");
  Object.entries(por).filter(([,p]) => p.vistos).sort((x,y) => (x[1].a/x[1].v) - (y[1].a/y[1].v)).forEach(([esp,p]) => {
    const pct = Math.round(p.a/p.v*100);
    const color = pct >= 70 ? "var(--ok)" : pct >= 50 ? "var(--warn)" : "var(--bad)";
    tbody.append(el("tr", {},
      el("td", { text:esp }),
      el("td", { class:"n" }, el("span", { class:"bar" }, el("i", { style:`width:${pct}%;background:${color}` })), `${pct} %`),
      el("td", { class:"n", text:`${p.vistos}/${p.total}` }),
      el("td", { class:"n", text:String(p.fall) })));
  });
  const sinTocar = Object.entries(por).filter(([,p]) => !p.vistos).map(([e]) => e);
  const hist = store.get("enarm.historial", []);
  const recientes = el("ul", { class:"review" });
  hist.slice(-8).reverse().forEach(h => recientes.append(el("li", {},
    el("span", { class:"mk " + (h.ok/h.n >= .6 ? "ok" : "bad"), text:"●" }),
    el("span", { text:h.esp }),
    el("span", { class:"note", text:`${h.ok}/${h.n} · ${new Date(h.t).toLocaleDateString("es-MX", { day:"numeric", month:"short" })}` }))));
  const borrar = el("button", { class:"btn", text:"Borrar mi progreso" });
  borrar.addEventListener("click", () => {
    if (borrar.dataset.confirm) { store.set("enarm.historial", []); store.set("enarm.preg", {}); renderProgreso(); return; }
    borrar.dataset.confirm = "1"; borrar.textContent = "Confirmar: borrar todo el progreso";
  });
  box.append(
    el("div", { class:"score" }, el("b", { text:`${vistos.length}/${BANCO.length}` }), el("span", { class:"muted", text:"reactivos del banco respondidos al menos una vez" })),
    el("div", {}, el("div", { class:"eyebrow", text:"Por especialidad (de menor a mayor acierto)" }),
      el("div", { class:"ptable" }, el("table", {},
        el("thead", {}, el("tr", {}, ...["Especialidad","Acierto","Vistos","Por repasar"].map(t => el("th", { text:t })))),
        tbody))),
    sinTocar.length ? el("p", { class:"note", text:"Sin empezar: " + sinTocar.join(", ") + "." }) : null,
    hist.length ? el("div", {}, el("div", { class:"eyebrow", text:"Últimos simulacros" }), recientes) : null,
    el("p", { class:"note", text:"El progreso se guarda solo en este navegador." }),
    el("div", {}, borrar));
}

/* ---------- Arranque ---------- */
calcular();
obtenerDatos().then(({ apuntes, banco }) => {
  construir(apuntes);
  BANCO = banco.filter(q => q && q.opciones && ["A","B","C","D"].every(l => q.opciones[l]) && q.opciones[q.correcta]);
  renderTOC(); llenarSelects();
  const prev = store.get("enarm.spec", null);
  abrir(SPECS.some(s => s.id === prev) ? prev : "estrategia");
  const tab = store.get("enarm.tab", "estudiar");
  if (tab !== "estudiar" && $("#view-" + tab)) show(tab);
}).catch(() => {
  $("#toc").textContent = "";
  $("#toc").append(el("p", { class:"note", text:"No se pudieron cargar los apuntes. Abre la versión autocontenida (repaso-enarm.html)." }));
});
})();

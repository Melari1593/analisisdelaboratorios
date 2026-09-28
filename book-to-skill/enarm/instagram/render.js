// Renderiza cada .slide de carrusel.html como PNG de 1080×1350 (formato 4:5 de Instagram).
// Uso: node render.js   (requiere Playwright instalado de forma global)
const { chromium } = require(require('child_process').execSync('npm root -g').toString().trim() + '/playwright');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1200, height: 1500 }, deviceScaleFactor: 1 });
  await p.goto('file://' + __dirname + '/carrusel.html');
  await p.evaluate(() => document.fonts.ready);
  const slides = await p.$$('.slide');
  for (let i = 0; i < slides.length; i++) {
    await slides[i].screenshot({ path: `${__dirname}/png/obstetricia-${String(i + 1).padStart(2, '0')}.png` });
  }
  const desborde = await p.$$eval('.slide', s => s.map((e, i) => [...e.querySelectorAll('*')].some(c => { const r = c.getBoundingClientRect(), R = e.getBoundingClientRect(); return r.bottom > R.bottom - 40 && c.closest('.foot') === null && !c.classList.contains('art') && !c.closest('svg'); }) ? i + 1 : 0).filter(Boolean));
  console.log('slides:', slides.length, 'desbordan:', desborde, 'fuentes:', await p.evaluate(() => [...document.fonts].filter(f => f.status === 'loaded').length));
  await b.close();
})();

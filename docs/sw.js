const CACHE = 'mapa-gr-v2.8.1';

// Essential assets cached on install
const CORE_ASSETS = [
  './',
  './index.html',
  './comparador.html',
  './manifest.json',
  './chart.umd.min.js',
  './help-doc.html',
  './estatisticas.html',
  './censo.html',
  './icons/icon-192.png',
  './icons/icon-512.png',
  './icons/icon-maskable-512.png',
  './dados/metadata.json',
  './dados/ies_publicas.json',  // índice das IES públicas (seletor de referência)
  './dados/exatas.json',  // default tab
  './dados/censo_superior_consolidado.json'
];

// Optional area JSONs cached on demand
const AREA_FILES = [
  './dados/biologicas.json',
  './dados/engenharias.json',
  './dados/saude.json',
  './dados/agrarias.json',
  './dados/sociais.json',
  './dados/humanas.json',
  './dados/letras.json',
  './dados/tecnologos.json'
];

self.addEventListener('install', (e) => {
  e.waitUntil(
    caches.open(CACHE)
      .then((c) => c.addAll(CORE_ASSETS))
      .then(() => self.skipWaiting())
  );
});

self.addEventListener('activate', (e) => {
  e.waitUntil(
    caches.keys().then((keys) =>
      Promise.all(keys.filter((k) => k !== CACHE).map((k) => caches.delete(k)))
    ).then(() => self.clients.claim())
  );
});

// Stale-while-revalidate for JSON data (dados/*.json)
// Network-first for the shell/HTML (mesma proteção do MAPA-PG): garante que
// atualizações de index.html e demais páginas cheguem assim que o usuário
// estiver online; offline cai no cache.
self.addEventListener('fetch', (e) => {
  const req = e.request;
  if (req.method !== 'GET') return;

  const url = new URL(req.url);
  const isJson = url.pathname.includes('/dados/') && url.pathname.endsWith('.json');

  if (isJson) {
    // stale-while-revalidate
    e.respondWith(
      caches.open(CACHE).then(async (cache) => {
        const cached = await cache.match(req);
        const fetchPromise = fetch(req).then((res) => {
          if (res && res.status === 200) cache.put(req, res.clone());
          return res;
        }).catch(() => cached);
        return cached || fetchPromise;
      })
    );
  } else {
    // network-first (atualiza o cache quando online; fallback ao cache offline)
    e.respondWith(
      fetch(req).then((res) => {
        if (res && res.status === 200 && res.type === 'basic') {
          const copy = res.clone();
          caches.open(CACHE).then((c) => c.put(req, copy));
        }
        return res;
      }).catch(() => caches.match(req))
    );
  }
});

#!/usr/bin/env python3
"""
Gerador da versão OFFLINE do MAPA-GR
====================================

Produz uma versão 100% local do aplicativo MAPA-GR — funciona abrindo
`index.html` diretamente do disco (file://), **sem servidor, sem internet,
sem instalação**, em qualquer navegador (Firefox, Chrome, Edge, Safari).

Estratégia: tudo encapsulado em HTML5.
  - Estilos: já são inline (<style>) nas páginas originais — preservados.
  - Chart.js: o <script src="chart.umd.min.js"> é substituído pelo conteúdo
    do arquivo, inline.
  - Dados: as chamadas fetch('dados/*.json') deixam de bater no disco —
    um shim de fetch inline devolve o JSON embutido no próprio HTML
    (window.__GR_DATA__). Isso evita o erro de CORS do Chrome em file://.
  - Ícone do cabeçalho: icons/icon-192.png vira um data: URI base64 inline.
  - Service Worker / manifest PWA: desativados (não fazem sentido offline).

Análogo ao create-offline-version.py do MAPA-PG, porém aqui TODO o conteúdo
(scripts, estilos e dados) fica encapsulado dentro de cada HTML5.

Uso:
    python3 gerar_offline.py            # lê ../docs/ , grava aqui
    python3 gerar_offline.py -s <src> -o <dest>
"""

import argparse
import base64
import json
import os
import re
import sys


def log(msg):     print(f"  {msg}")
def ok(msg):      print(f"✅ {msg}")
def warn(msg):    print(f"⚠️  {msg}")
def err(msg):     print(f"❌ {msg}")


# Áreas usadas pelas páginas de cursos (index / estatisticas / comparador)
AREA_SLUGS = ['exatas', 'biologicas', 'engenharias', 'saude', 'agrarias',
              'sociais', 'humanas', 'letras', 'tecnologos']


def escape_for_script(text):
    """Torna seguro embutir `text` dentro de um bloco <script>...</script>."""
    return (text.replace('</script', '<\\/script')
                .replace('<!--', '<\\!--')
                .replace(chr(0x2028), '\\u2028')
                .replace(chr(0x2029), '\\u2029'))


def build_data_block(src_dir, paths):
    """Monta um <script> que popula window.__GR_DATA__ e instala o shim de fetch.

    `paths` é a lista de caminhos relativos (ex.: 'dados/metadata.json')
    que a página solicita via fetch(); cada um é lido e embutido."""
    parts = ['<script>',
             '/* === MAPA-GR offline: dados embutidos + shim de fetch === */',
             'window.__GR_DATA__ = window.__GR_DATA__ || {};']
    for rel in paths:
        fp = os.path.join(src_dir, rel)
        with open(fp, 'r', encoding='utf-8') as f:
            raw = f.read()
        # valida que é JSON (e normaliza) — depois embute como literal JS
        json.loads(raw)
        safe = escape_for_script(raw)
        parts.append(f'window.__GR_DATA__[{json.dumps(rel)}] = {safe};')
        log(f"embutido {rel} ({len(raw)/1024/1024:.2f} MB)")
    # shim: intercepta fetch() dos caminhos locais; mantém fetch real p/ o resto
    parts.append("""(function(){
  var _f = window.fetch ? window.fetch.bind(window) : null;
  window.fetch = function(url){
    var key = (typeof url === 'string') ? url : (url && url.url);
    if (key && Object.prototype.hasOwnProperty.call(window.__GR_DATA__, key)) {
      var d = window.__GR_DATA__[key];
      return Promise.resolve({
        ok: true, status: 200,
        json: function(){ return Promise.resolve(d); },
        text: function(){ return Promise.resolve(JSON.stringify(d)); }
      });
    }
    if (_f) return _f.apply(this, arguments);
    return Promise.reject(new Error('offline: recurso indisponível: ' + key));
  };
})();""")
    parts.append('</script>')
    return '\n'.join(parts)


def transform(html, src_dir, chart_js, icon_uri, data_paths):
    """Aplica todas as transformações a uma página de cursos/censo."""
    # 1. Chart.js inline
    chart_inline = '<script>\n/* Chart.js 4.x (vendored, inline) */\n' \
                   + escape_for_script(chart_js) + '\n</script>'
    html = html.replace('<script src="chart.umd.min.js"></script>', chart_inline)

    # 2. Bloco de dados + shim de fetch (logo após o Chart.js inline)
    data_block = build_data_block(src_dir, data_paths)
    html = html.replace(chart_inline, chart_inline + '\n' + data_block, 1)

    # 3. Ícone do cabeçalho e <link rel="icon"> -> data URI
    html = html.replace('icons/icon-192.png', icon_uri)

    # 4. Remover <link rel="manifest"> (PWA não se aplica offline)
    html = re.sub(r'\s*<link rel="manifest"[^>]*>', '', html)

    # 5. Desativar Service Worker sem mexer no resto do bloco
    html = html.replace("'serviceWorker' in navigator",
                        "false /* offline: SW desativado */ && 'serviceWorker' in navigator")

    return html


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    ap = argparse.ArgumentParser(description='Gera a versão offline do MAPA-GR')
    ap.add_argument('-s', '--source', default=os.path.join(here, '..', 'docs'),
                    help='pasta fonte (padrão: ../mapa-gr/docs)')
    ap.add_argument('-o', '--output', default=here,
                    help='pasta destino (padrão: esta pasta)')
    args = ap.parse_args()

    src = os.path.abspath(args.source)
    out = os.path.abspath(args.output)
    print("\U0001f393 MAPA-GR — gerador da versão offline")
    print("=" * 52)

    if not os.path.isdir(src):
        err(f"pasta fonte não encontrada: {src}")
        sys.exit(1)
    os.makedirs(out, exist_ok=True)

    # Recursos compartilhados
    with open(os.path.join(src, 'chart.umd.min.js'), 'r', encoding='utf-8') as f:
        chart_js = f.read()
    with open(os.path.join(src, 'icons', 'icon-192.png'), 'rb') as f:
        icon_uri = 'data:image/png;base64,' + base64.b64encode(f.read()).decode('ascii')
    ok(f"Chart.js ({len(chart_js)/1024:.0f} KB) e ícone ({len(icon_uri)/1024:.0f} KB) carregados")

    # Páginas que usam metadata + todas as grandes áreas
    area_paths = ['dados/metadata.json'] + [f'dados/{s}.json' for s in AREA_SLUGS]
    pages = {
        # o seletor de referência do index.html busca o índice de IES públicas —
        # sem embuti-lo, o fetch cai no file:// e a lista abre vazia (bug v2.4)
        'index.html':        area_paths + ['dados/ies_publicas.json'],
        'estatisticas.html': area_paths,
        'comparador.html':   area_paths,
        'censo.html':        ['dados/censo_superior_consolidado.json'],
    }

    for name, paths in pages.items():
        print(f"\n→ {name}")
        with open(os.path.join(src, name), 'r', encoding='utf-8') as f:
            html = f.read()
        html = transform(html, src, chart_js, icon_uri, paths)
        dest = os.path.join(out, name)
        with open(dest, 'w', encoding='utf-8') as f:
            f.write(html)
        ok(f"{name} ({os.path.getsize(dest)/1024/1024:.1f} MB)")

    # help-doc.html é autossuficiente (apenas hyperlinks externos) -> cópia direta
    with open(os.path.join(src, 'help-doc.html'), 'r', encoding='utf-8') as f:
        help_html = f.read()
    with open(os.path.join(out, 'help-doc.html'), 'w', encoding='utf-8') as f:
        f.write(help_html)
    ok("help-doc.html (cópia direta)")

    total = sum(os.path.getsize(os.path.join(out, n)) for n in
                list(pages) + ['help-doc.html'])
    print("\n" + "=" * 52)
    ok(f"Versão offline gerada em: {out}")
    ok(f"Tamanho total dos HTML: {total/1024/1024:.1f} MB")
    print("\n→ Abra index.html diretamente no navegador (duplo clique).")


if __name__ == '__main__':
    main()

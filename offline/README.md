# MAPA-GR — Versão Offline (encapsulada em HTML5)

Versão 100% local do aplicativo **MAPA-GR** (análise da graduação
brasileira a partir dos indicadores SINAES/INEP — CPC, ENADE, IDD, IGC).
Funciona abrindo `index.html` **diretamente do disco** — sem servidor, sem
internet, sem instalação — em qualquer navegador (Firefox, Chrome, Edge,
Safari).

Diferente da versão online (`../docs`, um PWA com `fetch` + service
worker + Chart.js via CDN local), aqui **scripts, estilos e dados estão
todos encapsulados dentro de cada HTML5**. Cada arquivo `.html` é
autocontido.

## Como usar

Basta abrir **`index.html`** (duplo clique ou arrastar para o navegador).
A partir dele, os botões abrem as demais páginas:

| Arquivo            | Conteúdo                                             |
|--------------------|-----------------------------------------------------|
| `index.html`       | Painel principal — ranking, filtros, gráficos       |
| `estatisticas.html`| Estatísticas ENADE (todas as grandes áreas)         |
| `comparador.html`  | Comparar cursos entre UFs · TOP 10 (`?mode=top10`)  |
| `censo.html`       | Censo da Educação Superior 2017–2023                |
| `help-doc.html`    | Ajuda / documentação                                |

> **Chrome / Edge:** funciona direto via `file://` porque os dados são lidos
> de dentro do próprio HTML (não há `fetch` de arquivo local — o erro de CORS
> do Chrome não ocorre). Firefox e Safari idem.

Atalho por URL (igual à versão online), ex.:
`comparador.html?mode=top10`.

## O que foi encapsulado

| Aspecto         | Online (`../docs`)              | Offline (esta pasta)                 |
|-----------------|---------------------------------|--------------------------------------|
| Estilos         | inline (`<style>`)              | inline (`<style>`) — preservado      |
| Lógica          | inline (`<script>`)             | inline (`<script>`) — preservado     |
| Chart.js        | `<script src="chart.umd.min.js">` | conteúdo embutido inline           |
| Dados           | `fetch('dados/*.json')`         | embutidos em `window.__GR_DATA__` + shim de `fetch` |
| Ícone           | `icons/icon-192.png`            | `data:` URI base64 inline            |
| Service Worker  | `sw.js`                         | desativado                           |
| PWA / manifest  | `manifest.json`                 | removido                             |

O shim de `fetch` intercepta apenas os caminhos locais (`dados/*.json`) e
devolve o JSON embutido; qualquer outra URL continua usando o `fetch` real.
Por isso a lógica original das páginas **não precisou ser alterada**.

## Tamanho

| Arquivo            | Tamanho aprox. |
|--------------------|----------------|
| `index.html`       | ~17 MB         |
| `estatisticas.html`| ~17 MB         |
| `comparador.html`  | ~17 MB         |
| `censo.html`       | ~5,4 MB        |
| `help-doc.html`    | ~29 KB         |

Cada página de cursos embute as 9 grandes áreas (~47 mil cursos) + Chart.js.
O `censo.html` embute o consolidado 2017–2023. Disco total ~57 MB.

## Regenerar

Caso os dados em `../docs/dados/` sejam atualizados, regenere:

```bash
cd offline
python3 gerar_offline.py
```

O script lê `../docs/` (HTMLs, `chart.umd.min.js`, `icons/icon-192.png`
e os `dados/*.json`) e regrava as 5 páginas autocontidas nesta pasta.

## Autoria

Prof. David L. Azevedo — david888azv@unb.br

Software MAPA-GR. Dados públicos do [Portal de Dados Abertos do INEP](https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos).
Como citar: AZEVEDO, D. L. *MAPA-GR — um sistema interativo para
monitoramento e análise da graduação brasileira*. Physicae Organum, v. 11,
n. 1, 2026. DOI: 10.26512/2446-564X2026e62165.

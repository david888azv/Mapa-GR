#!/usr/bin/env python3
# Gera docs/dados/ies_publicas.json — instituições PÚBLICAS (federais, estaduais
# e municipais) da graduação, para o seletor de referência do MAPA-GR (busca por
# sigla/nome). Até a v2.4 o índice cobria apenas as federais (ies_federais.json).
#
# A chave é o CÓDIGO DA IES do INEP (campo `ci`), não a sigla: entre as públicas
# a sigla "FATEC" é usada por 5 instituições distintas e 7 instituições não têm
# sigla nenhuma. Agrupar por sigla fundiria umas e sumiria com outras.
import json, glob, os
from collections import Counter

# Categorias administrativas do INEP aceitas no seletor de referência.
CATEGORIAS = ('Pública Federal', 'Pública Estadual', 'Pública Municipal')

DOCS = os.path.join(os.path.dirname(__file__), '..', 'docs')
files = [f for f in glob.glob(os.path.join(DOCS, 'dados', '*.json'))
         if 'censo' not in os.path.basename(f) and 'metadata' not in os.path.basename(f)
         and not os.path.basename(f).startswith('ies_')]

inst = {}  # ci -> {nomes, siglas, cts, ufs, ccs}
for f in files:
    d = json.load(open(f, encoding='utf-8'))
    for c in d.get('cursos', []):
        ci = c.get('ci')
        if ci is None:
            continue
        it = inst.setdefault(ci, {'nomes': Counter(), 'siglas': Counter(),
                                  'cts': Counter(), 'ufs': Counter(), 'ccs': set()})
        if c.get('ie'):
            it['nomes'][c['ie']] += 1
        s = (c.get('sg') or '').strip()
        if s:
            it['siglas'][s] += 1
        if c.get('ct'):
            it['cts'][c['ct']] += 1
        if c.get('u'):
            it['ufs'][c['u']] += 1
        if c.get('cc') is not None:
            it['ccs'].add(c['cc'])


def top(counter, default=''):
    """Grafia mais frequente — o INEP varia caixa/pontuação entre os ciclos."""
    return counter.most_common(1)[0][0] if counter else default


pub = []
for ci, it in inst.items():
    ct = top(it['cts'])
    if ct in CATEGORIAS:
        pub.append({
            'ci': ci,                      # código INEP da IES — chave da referência
            'sigla': top(it['siglas']).upper(),
            'nome': top(it['nomes']) or str(ci),
            'uf': top(it['ufs']),
            'ct': ct,                      # esfera: exibida no seletor
            'n_cursos': len(it['ccs']),
        })

# ordena por nome (para leitura); a busca no cliente reordena por relevância
pub.sort(key=lambda x: x['nome'].upper())

out = {
    'gerado_em': '2026-08-08',
    'chave': 'ci',
    'categoria': 'Pública (federal, estadual e municipal)',
    'categorias': list(CATEGORIAS),
    'n_ies': len(pub),
    'ies': pub,
}
dest = os.path.join(DOCS, 'dados', 'ies_publicas.json')
json.dump(out, open(dest, 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
print(f'gerado {dest}: {len(pub)} IES públicas ({os.path.getsize(dest)/1024:.1f} KB)')

# sanity
por_esfera = Counter(i['ct'] for i in pub)
for k in CATEGORIAS:
    print(f'  {k:20s} {por_esfera.get(k, 0):4d}')
sem_sigla = [i for i in pub if not i['sigla']]
print(f'  sem sigla no INEP: {len(sem_sigla)} (exibidas pelo nome)')
dup = [s for s, n in Counter(i['sigla'] for i in pub if i['sigla']).items() if n > 1]
print(f'  siglas repetidas entre públicas: {dup or "nenhuma"}')
assert len({i['ci'] for i in pub}) == len(pub), 'código de IES duplicado'
for sig in ('UNB', 'UEMA', 'UNESP', 'UFMG'):
    hit = [i for i in pub if i['sigla'] == sig]
    print(f'  {sig}:', hit[0] if hit else 'AUSENTE na base INEP')

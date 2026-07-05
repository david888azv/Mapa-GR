#!/usr/bin/env python3
# Gera docs/dados/ies_federais.json — instituições PÚBLICAS FEDERAIS (IFES) da
# graduação, para o seletor de referência do MAPA-GR (busca por sigla/nome).
import json, glob, os
from collections import Counter

DOCS = os.path.join(os.path.dirname(__file__), '..', 'docs')
files = [f for f in glob.glob(os.path.join(DOCS, 'dados', '*.json'))
         if 'censo' not in os.path.basename(f) and 'metadata' not in os.path.basename(f)]

inst = {}  # sigla -> {nome, ct, ufs:Counter, ccs:set}
for f in files:
    d = json.load(open(f, encoding='utf-8'))
    for c in d.get('cursos', []):
        s = (c.get('sg') or '').upper().strip()
        if not s:
            continue
        it = inst.setdefault(s, {'nome': c.get('ie'), 'ct': c.get('ct'),
                                 'ufs': Counter(), 'ccs': set()})
        if c.get('u'):
            it['ufs'][c['u']] += 1
        if c.get('cc') is not None:
            it['ccs'].add(c['cc'])

fed = []
for s, it in inst.items():
    if 'federal' in (it['ct'] or '').lower():
        uf = it['ufs'].most_common(1)[0][0] if it['ufs'] else ''
        fed.append({
            'sigla': s,
            'nome': it['nome'] or s,
            'uf': uf,
            'n_cursos': len(it['ccs']),
        })

# ordena por nome (para leitura); a busca no cliente reordena por relevância
fed.sort(key=lambda x: x['nome'])

out = {
    'gerado_em': '2026-07-05',
    'categoria': 'Pública Federal (IFES)',
    'n_ies': len(fed),
    'ies': fed,
}
dest = os.path.join(DOCS, 'dados', 'ies_federais.json')
json.dump(out, open(dest, 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
print(f'gerado {dest}: {len(fed)} IFES federais')
# sanity
unb = [i for i in fed if i['sigla'] == 'UNB']
print('UNB presente:', bool(unb), unb[:1])
print('amostra:', [f"{i['sigla']}({i['uf']},{i['n_cursos']})" for i in fed[:8]])

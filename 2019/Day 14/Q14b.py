from math import ceil, floor

with open('Q14.txt', 'r') as f:
    prompt = f.read()

prompt = prompt.strip()
prompt = prompt.split('\n')

recs = {}
for k in prompt:
    rec = k.split('=>')
    rec[0] = rec[0].strip().split(',')
    rec[1] = rec[1].strip().split(' ')
    assert rec[1][1] not in recs
    recs[rec[1][1]] = {'num': int(rec[1][0]), 'ing': {}}
    for p in rec[0]:
        p = p.strip().split(' ')
        recs[rec[1][1]]['ing'][p[1]] = int(p[0])


def get_level(r, recs):
    if 'ORE' in recs[r]['ing']:
        return 1
    else:
        ret = 0
        for i in recs[r]['ing']:
            ret = max(ret, get_level(i, recs)) + 1
        return ret


for r in recs:
    recs[r]['lvl'] = get_level(r, recs)


def combine_ings(ingsa, ingsb):
    for k, v in ingsb.items():
        if k in ingsa:
            ingsa[k] += v
        else:
            ingsa[k] = v
    return ingsa


MAX_LVL = recs['FUEL']['lvl']
MAX_ORE = 1000000000000

num_fuel = floor(MAX_ORE/720484) #from part a
last = None

while True:
    ings = recs['FUEL']['ing'].copy()

    for k in ings:
        ings[k] = ings[k] * ceil(num_fuel/recs['FUEL']['num'])
    for i in range(MAX_LVL, 0, -1):
        dec = {}
        rem = set()
        for k in ings:
            if recs[k]['lvl'] == i:
                brk = recs[k]['ing'].copy()
                for p in brk:
                    brk[p] = brk[p] * ceil(ings[k]/recs[k]['num'])
                dec = combine_ings(dec, brk)
                rem.add(k)
        for k in rem:
            ings.pop(k)
        ings = combine_ings(ings, dec)
    if ings['ORE'] > MAX_ORE:
        num_fuel -= 1
        break
    else:
        num_fuel += 1

print(num_fuel)

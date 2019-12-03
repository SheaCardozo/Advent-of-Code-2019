with open('Q3.txt', 'r') as f:
    prompt = f.read()

prompt = prompt.strip()
prompt = prompt.split('\n')

wa = prompt[0].split(',')
wb = prompt[1].split(',')

pa = dict()
c = (0, 0)
ct = 1
for k, i in enumerate(wa):
    d = i[0]
    if d == 'R':
        d = (1, 0)
    elif d == 'L':
        d = (-1, 0)
    elif d == 'U':
        d = (0, 1)
    else:
        d = (0, -1)

    q = int(i[1:])
    for t in range(1, q+1):
        vi = (c[0] + d[0] * t, c[1] + d[1] * t)
        pa[vi] = ct
        ct += 1
    c = vi

pb = set()
c = (0, 0)
ct = 1
for k, i in enumerate(wb):
    d = i[0]
    if d == 'R':
        d = (1, 0)
    elif d == 'L':
        d = (-1, 0)
    elif d == 'U':
        d = (0, 1)
    else:
        d = (0, -1)

    q = int(i[1:])
    for t in range(1,q+1):
        vi = (c[0] + d[0] * t, c[1] + d[1] * t)
        if vi in pa:
            pb.add((ct + pa[vi], vi))
        ct += 1
    c = vi

steps = None

for i in pb:
    if steps is None:
        steps = i[0]
    else:
        steps = min(steps, i[0])

if steps is None:
    print('error')
print(steps)


with open('Q3.txt', 'r') as f:
    prompt = f.read()

prompt = prompt.strip()
prompt = prompt.split('\n')
wa = prompt[0].split(',')
wb = prompt[1].split(',')
pa = set()
c = (0, 0)
for i in wa:
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
        pa.add(vi)
    c = vi

pb = set()
c = (0, 0)
for i in wb:
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
            pb.add(vi)
    c = vi

dist = None


for i in pb:
    if dist is None:
        dist = abs(i[0]) + abs(i[1])
    else:
        dist = min(dist, abs(i[0]) + abs(i[1]))

if dist is None:
    print('error')
print(dist)


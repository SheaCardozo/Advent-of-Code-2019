from math import acos, sqrt, pi

with open('Q10.txt', 'r') as op:
    prompt = op.read()

prompt = prompt.split()

rocks = {}

for y, l in enumerate(prompt):
    for x, a in enumerate(l):
        if a == '#':
            rocks[(x, y)] = 0

sees = {}

k = (26, 36)
for c in rocks:
    if k == c:
        continue

    see = True

    m = max(abs(c[0] - k[0]), abs(c[1] - k[1]))
    d = (c[0] - k[0], c[1] - k[1])
    for i in range(1, m):
        q = (k[0] + d[0] * i / m, k[1] + d[1] * i / m)
        if q[0].is_integer() and q[1].is_integer():
            if (int(q[0]), int(q[1])) in rocks:
                see = False

    if see:
        sees[c] = abs(acos((k[1] - c[1])/(sqrt((c[1] - k[1]) ** 2 + (c[0] - k[0]) ** 2))) - (2*pi if c[0] < k[0] else 0))


angles = []
for p in sees:
    angles.append(sees[p])

bet = sorted(angles)[199]
for p in sees:
    if sees[p] == bet:
        print(p[0]*100 + p[1])

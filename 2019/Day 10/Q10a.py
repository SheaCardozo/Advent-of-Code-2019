with open('Q10.txt', 'r') as f:
    prompt = f.read()

prompt = prompt.split()

rocks = {}

for y, l in enumerate(prompt):
    for x, a in enumerate(l):
        if a == '#':
            rocks[(x, y)] = 0

for k in rocks:
    for c in rocks:
        if k == c:
            continue

        see = True

        m = max(abs(c[0] - k[0]), abs(c[1] - k[1]))
        d = (c[0] - k[0], c[1] - k[1])
        for i in range(1, m):
            q = (k[0] + d[0] * i / m, k[1] + d[1] * i / m)
            if q[0].is_integer() and q[1].is_integer():
                if (q[0], q[1]) in rocks:
                    see = False

        if see:
            rocks[k] += 1

opt = None
for k, v in rocks.items():
    if opt is None or v > rocks[opt]:
        opt = k

print(rocks[opt])

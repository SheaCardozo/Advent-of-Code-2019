with open('Q8.txt', 'r') as op:
    prompt = op.read()

prompt = prompt.strip()
minz = None
mino = None
mint = None
for i in range(0, len(prompt), 150):
    z = 0
    o = 0
    t = 0

    for j in prompt[i:i+150]:
        j = int(j)
        if j == 0:
            z += 1
        elif j == 1:
            o += 1
        elif j == 2:
            t += 1

    if minz is None or z < minz:
        minz, mino, mint = z, o, t

print(mino * mint)
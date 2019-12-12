with open('Q12.txt', 'r') as f:
    prompt = f.read()

prompt = prompt.strip().split('\n')

for i, v in enumerate(prompt):
    v = v.strip('<>')
    v = v.split()
    v = [[int(''.join(c for c in k if c.isdigit() or c == '-')) for k in v], [0, 0, 0]]
    prompt[i] = v


def unit(n):
    return n / abs(n) if n else 0


def apply_gravity(moons):
    index = list(range(len(moons)))
    pairs = []
    for j in index:
        pairs.extend([(i, j) for i in index if i != j])

    for i, j in pairs:
        moons[i][1][0] += unit(moons[j][0][0] - moons[i][0][0])
        moons[i][1][1] += unit(moons[j][0][1] - moons[i][0][1])
        moons[i][1][2] += unit(moons[j][0][2] - moons[i][0][2])


def move(moons):
    for i, v in enumerate(moons):
        moons[i][0][0] += moons[i][1][0]
        moons[i][0][1] += moons[i][1][1]
        moons[i][0][2] += moons[i][1][2]


for i in range(0, 1000):
    apply_gravity(prompt)
    move(prompt)

e = 0

for i in prompt:
    pot = abs(i[0][0]) + abs(i[0][1]) + abs(i[0][2])
    kin = abs(i[1][0]) + abs(i[1][1]) + abs(i[1][2])
    e += pot*kin

print(e)
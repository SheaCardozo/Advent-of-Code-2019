from math import gcd
from copy import deepcopy

with open('Q12.txt', 'r') as f:
    prompt = f.read()

prompt = prompt.strip().split('\n')

for i, v in enumerate(prompt):
    v = v.strip('<>')
    v = v.split()
    v = [[int(''.join(c for c in k if c.isdigit() or c == '-')) for k in v], [0, 0, 0]]
    prompt[i] = v


def get_key(moons, axis):
    p = ""
    for i in moons:
        for j in i:
            p += str(j[axis])
    return p


def unit(n):
    return int(n / abs(n) if n else 0)


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


steps = []

for i in range(3):
    moons = deepcopy(prompt)
    past_pos = dict()
    step = 0
    while True:
        k = get_key(moons, i)
        if k in past_pos:
            break
        past_pos[k] = step
        apply_gravity(moons)
        move(moons)
        step += 1
    steps.append((step - past_pos[k], past_pos[k]))

offset = max([off[1] for off in steps])


def lcm(a, b):
    a, b = int(a), int(b)
    return a * b / gcd(a, b)


ans = lcm(steps[0][0], lcm(steps[1][0], steps[2][0]))
ans += offset
print(ans)

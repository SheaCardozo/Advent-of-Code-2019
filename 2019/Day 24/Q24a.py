with open('Q24.txt', 'r') as f:
    prompt = f.read()

prompt = prompt.strip()
prompt = prompt.split('\n')


bugs = []

for i in prompt:
    bugs.append([])
    for j in i:
        bugs[-1].append(j)


def get_bug(i, j, bugs):
    if 0 <= i < len(bugs) and 0 <= j < len(bugs[i]):
        return 1 if bugs[i][j] == '#' else 0
    else:
        return 0


def num_bugs(i, j, bugs):
    num = 0
    num += get_bug(i + 1, j, bugs)
    num += get_bug(i - 1, j, bugs)
    num += get_bug(i, j + 1, bugs)
    num += get_bug(i, j - 1, bugs)
    return num


def update(bugs):
    new = []
    for i in range(len(bugs)):
        new.append([])
        for j in range(len(bugs[i])):
            if num_bugs(i, j, bugs) == 1:
                new[-1].append('#')
            elif num_bugs(i, j, bugs) == 2:
                new[-1].append('#' if bugs[i][j] == '.' else '.')
            else:
                new[-1].append('.')
    return new


pos = set()

while True:
    key = ''
    for i in bugs:
        for j in i:
            key += j

    if key in pos:
        break

    pos.add(key)

    bugs = update(bugs)

p = 0
bio = 0
for i in bugs:
    for j in i:
        bio += pow(2, p) if j == '#' else 0
        p += 1

print(bio)

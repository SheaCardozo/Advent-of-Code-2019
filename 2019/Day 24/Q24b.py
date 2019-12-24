with open('Q24.txt', 'r') as f:
    prompt = f.read()

prompt = prompt.strip()
prompt = prompt.split('\n')


class DuelList:

    def __init__(self):
        self.right = [[]]
        self.left = [[]]

        for i in range(5):
            self.right[0].append([])
            for j in range(5):
                self.right[0][-1].append('.')

    def __getitem__(self, key):
        if key < 0:
            return self.left[-key]
        else:
            return self.right[key]

    def __setitem__(self, key, item):
        if key < 0:
            self.left[-key] = item
        else:
            self.right[key] = item

    def add_layer(self):
        self.left.append([])
        self.right.append([])

        for i in range(5):
            self.right[-1].append([])
            self.left[-1].append([])
            for j in range(5):
                self.right[-1][-1].append('.')
                self.left[-1][-1].append('.')

    def __len__(self):
        return len(self.right)


bugs = DuelList()

for i in range(len(prompt)):
    for j in range(len(prompt[i])):
        bugs[0][i][j] = prompt[i][j]

bugs.add_layer()


def get_bug(z, i, j, bugs, tag):
    try:
        if i == 2 and j == 2:
            if tag == 'u':
                return sum([1 if x == '#' else 0 for x in bugs[z-1][-1]])
            if tag == 'd':
                return sum([1 if x == '#' else 0 for x in bugs[z-1][0]])
            if tag == 'r':
                ans = 0
                for x in bugs[z-1]:
                    ans += 1 if x[0] == '#' else 0
                return ans
            if tag == 'l':
                ans = 0
                for x in bugs[z-1]:
                    ans += 1 if x[-1] == '#' else 0
                return ans
        elif i >= 5:
            return 1 if bugs[z+1][3][2] == '#' else 0
        elif i < 0:
            return 1 if bugs[z+1][1][2] == '#' else 0
        elif j >= 5:
            return 1 if bugs[z+1][2][3] == '#' else 0
        elif j < 0:
            return 1 if bugs[z+1][2][1] == '#' else 0
        else:
            return 1 if bugs[z][i][j] == '#' else 0
    except IndexError:
        return 0


def num_bugs(z, i, j, bugs):
    num = 0
    num += get_bug(z, i + 1, j, bugs, 'd')
    num += get_bug(z, i - 1, j, bugs, 'u')
    num += get_bug(z, i, j + 1, bugs, 'r')
    num += get_bug(z, i, j - 1, bugs, 'l')
    return num


def update(bugs):
    new = DuelList()
    for p in range(len(bugs)):
        todo = set([p, -p])
        new.add_layer()
        for z in todo:
            for i in range(len(bugs[z])):
                for j in range(len(bugs[z][i])):
                    if i == 2 and j == 2:
                        continue
                    b = num_bugs(z, i, j, bugs)
                    if b == 1:
                        new[z][i][j] = '#'
                    elif b == 2:
                        new[z][i][j] = '#' if bugs[z][i][j] == '.' else '.'
                    else:
                        new[z][i][j] = '.'
    return new


for i in range(200):
    bugs = update(bugs)

ans = 0
for p in range(len(bugs)):
    todo = set([p, -p])
    for z in todo:
        for i in bugs[z]:
            for j in i:
                if j == '#':
                    ans += 1

print(ans)
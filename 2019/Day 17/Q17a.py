from utils import Intcode

with open('Q17.txt', 'r') as f:
    prompt = f.read()

prompt = prompt.strip()
prompt = prompt.split(',')

prompt = list(map(int, prompt))

field = [[]]


class Part17a(Intcode):

    def _input(self):
        return 0

    def _output(self, out):
        global field

        out = chr(out)
        if out == '\n':
            field.append([])
        else:
            field[-1].append(out)
        return


ic = Part17a(prompt)
ic.run()

while True:
    if len(field[-1]) == 0:
        field = field[:-1]
    else:
        break

ans = 0

for y in range(1, len(field) - 1):
    for x in range(1, len(field[0]) - 1):
        if all([p == '#' for p in (field[y][x], field[y + 1][x], field[y - 1][x], field[y][x + 1], field[y][x - 1])]):
            ans += x * y

print(ans)

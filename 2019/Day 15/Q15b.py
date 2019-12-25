from utils import Intcode
from random import randint

with open('Q15.txt', 'r') as f:
    prompt = f.read()

prompt = prompt.strip()
prompt = prompt.split(',')

prompt = list(map(int, prompt))

tiles = dict()

pos = (0, 0)
oxy = False
tiles = {}
count = 0

tried = set()

prevm = None

movements = []


def get_shortest_path(m):
    movements = m
    while True:
        done = True
        n = []
        i = 0
        while True:
            if i > len(movements) - 1:
                break
            elif i == len(movements) - 1:
                n.append(movements[-1])
                break
            a = movements[i]
            b = movements[i + 1]

            if a + b == 3 or a + b == 7:
                i += 1
                done = False
            else:
                n.append(a)

            i += 1
        movements = n
        if done:
            break
    return len(movements)


class Part15b(Intcode):

    def _input(self):
        global prevm
        m = None
        while m is None or m in tried:
            m = randint(1, 4)
        tried.add(m)
        prevm = m
        return m

    def _output(self, out):
        global oxy
        global tried
        global prevm
        global pos
        global movements
        global count
        if out == 2 and not oxy:
            movements = []
            oxy = True
        elif out == 1 or out == 2:
            tried.clear()
            if oxy:
                movements.append(prevm)
            if prevm == 1:
                pos = pos[0], pos[1] - 1
                prevm = 2
            elif prevm == 2:
                pos = pos[0], pos[1] + 1
                prevm = 1
            elif prevm == 3:
                pos = pos[0] - 1, pos[1]
                prevm = 4
            else:
                pos = pos[0] + 1, pos[1]
                prevm = 3
            if oxy:
                if pos in tiles:
                    count += 1
                    if count > 1000000:
                        raise EOFError
                else:
                    tiles[pos] = get_shortest_path(movements)
                    count = 0
            tried.add(prevm)
        elif out == 0:
            if len(tried) == 4:
                tried.clear()


ic = Part15b(prompt)
ic.run()

m = max([tiles[i] for i in tiles])
print(m)

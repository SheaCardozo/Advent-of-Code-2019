from utils import Intcode
from random import randint

with open('Q15.txt', 'r') as f:
    prompt = f.read()

prompt = prompt.strip()
prompt = prompt.split(',')

prompt = list(map(int, prompt))

tiles = dict()

pos = (0, 0)
oxy = None

tried = set()

prevm = None

movements = []


class Part15a(Intcode):

    def _input(self):
        global pos
        global prevm
        m = None
        while m is None or m in tried:
            m = randint(1, 4)
        tried.add(m)
        prevm = m
        if m == 1:
            pos = pos[0], pos[1] - 1
        elif m == 2:
            pos = pos[0], pos[1] + 1
        elif m == 3:
            pos = pos[0] - 1, pos[1]
        else:
            pos = pos[0] + 1, pos[1]
        return m

    def _output(self, out):
        global oxy
        global tried
        global prevm
        if out == 2:
            movements.append(prevm)
            oxy = pos
            raise EOFError
        elif out == 1:
            movements.append(prevm)
            tried.clear()
            if prevm == 1:
                prevm = 2
            elif prevm == 2:
                prevm = 1
            elif prevm == 3:
                prevm = 4
            else:
                prevm = 3
            tried.add(prevm)
        elif out == 0:
            if len(tried) == 4:
                tried.clear()


ic = Part15a(prompt)
ic.run()


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
        b = movements[i+1]

        if a + b == 3 or a + b == 7:
            i += 1
            done = False
        else:
            n.append(a)

        i += 1
    movements = n
    if done:
        break

print(len(movements))

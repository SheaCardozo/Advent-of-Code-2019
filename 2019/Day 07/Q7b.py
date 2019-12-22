from itertools import permutations
from utils import Intcode


with open('Q7.txt', 'r') as f:
    prompt = f.read()

prompt = prompt.strip()
prompt = prompt.split(',')

prompt = list(map(int, prompt))


class Part7b(Intcode):

    def _input(self):
        r = i[k] if self.input == 0 else inp
        self.input = 1
        return r

    def _output(self, out):
        global inp, cont
        inp, cont = out, True
        self.i += 2
        raise EOFError


ans = None

trials = list(permutations([9, 8, 7, 6, 5]))
for i in trials:
    amps = []
    for p in range(5):
        amps.append(Part7b(prompt.copy()))

    inp = 0
    k = 0
    cont = True

    while cont:
        cont = False
        amps[k].run()
        k = (k + 1) % len(amps)

    ans = inp if ans is None else max(ans, inp)

print(ans)

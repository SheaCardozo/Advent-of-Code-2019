from itertools import permutations
from utils import Intcode


with open('Q7.txt', 'r') as op:
    prompt = op.read()

prompt = prompt.strip()
prompt = prompt.split(',')

prompt = list(map(int, prompt))


class Part7a(Intcode):

    def _input(self):
        r = j if self.input == 0 else inp
        self.input += 1
        return r

    def _output(self, out):
        global inp
        inp = out


ans = None

trials = list(permutations([0, 1, 2, 3, 4]))

for i in trials:
    codes = prompt.copy()
    inp = 0
    for j in i:
        ic = Part7a(codes)
        ic.run()
    ans = inp if ans is None else max(ans, inp)

print(ans)

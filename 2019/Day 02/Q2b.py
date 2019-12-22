from utils import Intcode

with open('Q2.txt', 'r') as f:
    prompt = f.read()

prompt = prompt.strip()
prompt = prompt.split(',')

prompt = list(map(int, prompt))


class Part2b(Intcode):

    def _input(self):
        return 0

    def _output(self, out):
        pass


for p in range(100):
    for q in range(100):
        codes = prompt.copy()
        codes[1] = p
        codes[2] = q

        ic = Part2b(codes)
        ic.run()

        if ic.codes[0] == 19690720:
            print(p*100 + q)
            break

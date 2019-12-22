from utils import Intcode

with open('Q2.txt', 'r') as f:
    prompt = f.read()

prompt = prompt.strip()
prompt = prompt.split(',')

prompt = list(map(int, prompt))

prompt[1] = 12
prompt[2] = 2


class Part2a(Intcode):

    def _input(self):
        return 0

    def _output(self, out):
        pass


ic = Part2a(prompt)
ic.run()
print(ic.codes[0])


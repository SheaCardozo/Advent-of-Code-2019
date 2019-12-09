from utils import Intcode

with open('Q9.txt', 'r') as op:
    prompt = op.read()

prompt = prompt.strip()
prompt = prompt.split(',')

prompt = list(map(int, prompt))


class Part9b(Intcode):

    def _input(self):
        return 2

    def _output(self, out):
        print(out)


ic = Part9b(prompt)
ic.run()

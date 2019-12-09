from utils import Intcode

with open('Q5.txt', 'r') as op:
    prompt = op.read()

prompt = prompt.strip()
prompt = prompt.split(',')

prompt = list(map(int, prompt))


class Part5a(Intcode):

    def _input(self):
        return 1

    def _output(self, out):
        print(out)


ic = Part5a(prompt)
ic.run()

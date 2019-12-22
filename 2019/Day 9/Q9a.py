from utils import Intcode

with open('Q9.txt', 'r') as f:
    prompt = f.read()

prompt = prompt.strip()
prompt = prompt.split(',')

prompt = list(map(int, prompt))


class Part9a(Intcode):

    def _input(self):
        return 1

    def _output(self, out):
        print(out)


ic = Part9a(prompt)
ic.run()

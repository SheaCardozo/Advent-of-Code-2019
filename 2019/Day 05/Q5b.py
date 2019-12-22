from utils import Intcode

with open('Q5.txt', 'r') as f:
    prompt = f.read()

prompt = prompt.strip()
prompt = prompt.split(',')

prompt = list(map(int, prompt))


class Part5b(Intcode):

    def _input(self):
        return 5

    def _output(self, out):
        print(out)


ic = Part5b(prompt)
ic.run()

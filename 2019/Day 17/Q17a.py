from utils import Intcode

with open('Q17.txt', 'r') as f:
    prompt = f.read()

prompt = prompt.strip()
prompt = prompt.split(',')

prompt = list(map(int, prompt))


class Part17a(Intcode):

    def _input(self):
        return 0

    def _output(self, out):
        print(out)
        return


ic = Part17a(prompt)
ic.run()


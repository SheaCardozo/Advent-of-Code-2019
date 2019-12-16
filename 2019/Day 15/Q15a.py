from utils import Intcode

with open('Q15.txt', 'r') as op:
    prompt = op.read()

prompt = prompt.strip()
prompt = prompt.split(',')

prompt = list(map(int, prompt))

tiles = dict()

points = []
movements = [(0, 0)]

moves = [1, 2, 3, 4]

movecount = None

class Part15a(Intcode):

    def _input(self):
        if movements[-1] = 4:
        return 0

    def _output(self, out):
        if out == 0:


ic = Part15a(prompt)
ic.run()


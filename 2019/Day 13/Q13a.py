from utils import Intcode

with open('Q13.txt', 'r') as op:
    prompt = op.read()

prompt = prompt.strip()
prompt = prompt.split(',')

prompt = list(map(int, prompt))

tiles = dict()

inp = []


class Part13a(Intcode):

    def _input(self):
        return 0

    def _output(self, out):
        global tiles
        global inp

        inp.append(out)

        if len(inp) == 3:
            tiles[(inp[0], inp[1])] = inp[2]
            inp = []


ic = Part13a(prompt)
ic.run()

print(sum([tiles[b] == 2 for b in tiles]))

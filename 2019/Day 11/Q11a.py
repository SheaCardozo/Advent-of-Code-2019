from utils import Intcode

with open('Q11.txt', 'r') as f:
    prompt = f.read()

prompt = prompt.strip()
prompt = prompt.split(',')

prompt = list(map(int, prompt))

pos = 0, 0
turn = 0, 1
tiles = {}
outtype = False

class Part11a(Intcode):

    def _input(self):
        return tiles.get(pos, 0)

    def _output(self, out):
        global outtype
        global pos
        global tiles
        global turn

        if outtype:
            out = -1 if out == 0 else out
            if turn[0] == 0:
                turn = out * turn[1], 0
            else:
                turn = 0, -out * turn[0]

            pos = pos[0] + turn[0],  pos[1] + turn[1]

        else:
            tiles[pos] = out

        outtype = not outtype


ic = Part11a(prompt)
ic.run()

print(len(tiles))

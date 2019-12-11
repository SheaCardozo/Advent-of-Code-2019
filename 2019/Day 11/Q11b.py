from utils import Intcode

with open('Q11.txt', 'r') as op:
    prompt = op.read()

prompt = prompt.strip()
prompt = prompt.split(',')

prompt = list(map(int, prompt))

pos = 0, 0
turn = 0, 1
tiles = {pos: 1}
outtype = False


class Part11b(Intcode):

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


ic = Part11b(prompt)
ic.run()

minx = None
maxx = None
miny = None
maxy = None

for k in tiles:
    minx = k[0] if minx is None else min(minx, k[0])
    maxx = k[0] if maxx is None else max(maxx, k[0])
    miny = k[1] if miny is None else min(miny, k[1])
    maxy = k[0] if maxy is None else max(maxy, k[0])


for y in range(maxy, miny-1, -1):
    p = ["#" if tiles.get((x, y), 0) == 1 else " " for x in range(minx, maxx+1)]
    if any(n == "#" for n in p):
        print(p)

from utils import Intcode
import cmath

with open('Q17.txt', 'r') as f:
    prompt = f.read()

prompt = prompt.strip()
prompt = prompt.split(',')

prompt = list(map(int, prompt))

#Used to find A,B,C
'''
field = [[]]


class Part17a(Intcode):

    def _input(self):
        return 0

    def _output(self, out):
        global field

        out = chr(out)
        if out == '\n':
            field.append([])
        else:
            field[-1].append(out)
        return


ic = Part17a(prompt)
ic.run()

while True:
    if len(field[-1]) == 0:
        field = field[:-1]
    else:
        break

bot = None
face = -1+0j

for y in range(len(field)):
    for x in range(len(field[0])):
        if field[y][x] == '^':
            bot = x, y

path = []

for x in field:
    print("".join(x))


def inbounds(lst, y, x, k):
    if 0 <= y < len(lst):
        if 0 <= x < len(lst[0]):
            return lst[y][x] == k
    return False


while True:
    if inbounds(field, bot[1] + int(face.real), bot[0] + int(face.imag), '#'):
        path[-1] += 1
        bot = bot[0] + int(rot.imag), bot[1] + int(rot.real)
    else:
        rot = face * 1j
        if inbounds(field, bot[1] + int(rot.real), bot[0] + int(rot.imag), '#'):
            face = rot
            path.append('L')
            path.append(0)
            continue
        rot = face * -1j
        if inbounds(field, bot[1] + int(rot.real), bot[0] + int(rot.imag), '#'):
            face = rot
            path.append('R')
            path.append(0)
            continue
        break

'''
prompt[0] = 2

A = 'R,8,L,12,R,8\n'
B = 'L,10,L,10,R,8\n'
C = 'L,12,L,12,L,10,R,10\n'

path = 'A,A,B,C,B,C,B,A,C,A\n'

inp = path + A + B + C + 'n\n'

i = -1


class Part17b(Intcode):

    def _input(self):
        global i
        i += 1
        print(ord(inp[i]))
        return ord(inp[i])

    def _output(self, out):
        print(out)


ic = Part17b(prompt)
ic.run()

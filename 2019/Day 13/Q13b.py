from utils import Intcode

with open('Q13.txt', 'r') as op:
    prompt = op.read()

prompt = prompt.strip()
prompt = prompt.split(',')

prompt = list(map(int, prompt))

prompt[0] = 2

tiles = dict()

inp = []

ball = None

paddle = None

score = 0


class Part13b(Intcode):

    def _input(self):
        if ball[0] > paddle[0]:
            return 1
        elif ball[0] < paddle[0]:
            return -1
        else:
            return 0

    def _output(self, out):
        global tiles
        global inp
        global score
        global paddle
        global ball

        inp.append(out)

        if len(inp) == 3:
            if inp[0] == -1 and inp[1] == 0:
                score = inp[2]
            elif inp[2] == 3:
                paddle = (inp[0], inp[1])
            elif inp[2] == 4:
                ball = (inp[0], inp[1])
            else:
                tiles[(inp[0], inp[1])] = inp[2]
            inp = []


ic = Part13b(prompt)
ic.run()

print(score)
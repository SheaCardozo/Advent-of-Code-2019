from utils import Intcode

with open('Q19.txt', 'r') as f:
    prompt = f.read()

prompt = prompt.strip()
prompt = prompt.split(',')

prompt = list(map(int, prompt))

points = []


class Part19a(Intcode):

    def _input(self):
        global ok
        ok = not ok
        if ok:
            return a

        return b

    def _output(self, out):
        global points
        points.append(out)


for a in range(50):
    for b in range(50):
        ok = False
        ic = Part19a(prompt.copy())
        ic.run()

print(sum(points))

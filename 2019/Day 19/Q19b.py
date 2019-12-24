from utils import Intcode

with open('Q19.txt', 'r') as f:
    prompt = f.read()

prompt = prompt.strip()
prompt = prompt.split(',')

prompt = list(map(int, prompt))

points = []


class Part19b(Intcode):

    def _input(self):
        global ok
        ok = not ok
        if ok:
            return a

        return b

    def _output(self, out):
        global ans
        ans = out


def istractor():
    global ans
    global ok
    ok = False
    ic = Part19b(prompt.copy())
    ic.run()
    return ans


point = None
y = 100
nextx = 100
while y < 10000:
    x = nextx
    skip = False
    if point is not None:
        break
    while x < 10000:
        a, b = x, y
        if istractor():
            if not skip:
                nextx = x
            skip = True
            a, b = x, y + 99
            if istractor():
                a, b = x + 99, y
                if istractor():
                    check = True
                    for a in range(x, x+100):
                        for b in range(y, y+100):
                            check = check and istractor()
                    if check:
                        point = x, y
                        break
        elif skip:
            break
        x += 1
    y += 1

print(point[0] * 10000 + point[1])


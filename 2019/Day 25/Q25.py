from utils import Intcode

with open('Q25.txt', 'r') as f:
    prompt = f.read()

prompt = prompt.strip()
prompt = prompt.split(',')

prompt = list(map(int, prompt))

inp = ""
otp = ""


class Part25a(Intcode):

    def _input(self):
        global inp
        global otp
        if len(inp) == 0:
            print(otp)
            otp = ""
            inp = input()
            inp += '\n'
        r = inp[0]
        inp = inp[1:]
        return ord(r)

    def _output(self, out):
        global otp

        otp += chr(out)


ic = Part25a(prompt)
ic.run()

print(otp)

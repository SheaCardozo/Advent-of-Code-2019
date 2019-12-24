from utils import Intcode

with open('Q21.txt', 'r') as f:
    prompt = f.read()

prompt = prompt.strip()
prompt = prompt.split(',')

prompt = list(map(int, prompt))

output = ""
# Jump if there is a hole between one and three tiles away, and there's ground four tiles away,
# and if there's no hole five tiles away ensure there is ground 8 tiles away
input = '''NOT A T
OR T J
NOT B T
OR T J
NOT C T
OR T J
AND D J
NOT E T
NOT T T
OR H T
AND T J
RUN
'''
inind = -1


class Part21b(Intcode):

    def _input(self):
        global inind

        inind += 1
        return ord(input[inind])

    def _output(self, out):
        global output

        output += str(out) if out >= 128 else chr(out)


ic = Part21b(prompt)
ic.run()

print(output)

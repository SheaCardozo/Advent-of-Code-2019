from utils import Intcode


with open('Q23.txt', 'r') as f:
    prompt = f.read()

prompt = prompt.strip()
prompt = prompt.split(',')

prompt = list(map(int, prompt))

reqs = {}

special_package = None


class Part23a(Intcode):

    def __init__(self, codes, nid):
        self.codes = codes
        self.i = 0
        self.base = 0
        self.nid = nid
        self.input = [];

    def _input(self):
        global reqs
        reqs[self.nid]['halt'] = not reqs[self.nid]['halt']
        if reqs[self.nid]['halt']:
            raise EOFError
        if len(reqs[self.nid]['inputs']) == 0:
            return -1
        r = reqs[self.nid]['inputs'][0]
        reqs[self.nid]['inputs'] = reqs[self.nid]['inputs'][1:]
        return r

    def _output(self, out):
        global reqs
        global special_package
        self.input.append(out)

        if len(self.input) == 3:
            if self.input[0] == 255:
                special_package = self.input[2]
                raise EOFError
            reqs[self.input[0]]['inputs'].append(self.input[1])
            reqs[self.input[0]]['inputs'].append(self.input[2])
            self.input = []


network = []

for i in range(50):
    reqs[i] = {}
    reqs[i]['halt'] = False
    reqs[i]['inputs'] = [i]

    network.append(Part23a(prompt.copy(), i))

while special_package is None:
    for ic in network:
        ic.run()

print(special_package)


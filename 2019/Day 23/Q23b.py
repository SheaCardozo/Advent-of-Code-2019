from utils import Intcode
from copy import deepcopy


with open('Q23.txt', 'r') as f:
    prompt = f.read()

prompt = prompt.strip()
prompt = prompt.split(',')

prompt = list(map(int, prompt))

reqs = {}

special_package = None, None
idle = False
sent = set()


class Part23a(Intcode):

    def __init__(self, codes, nid):
        self.codes = codes
        self.i = 0
        self.base = 0
        self.nid = nid
        self.input = []

    def _input(self):
        global reqs
        global special_package
        global idle
        global sent
        reqs[self.nid]['halt'] = not reqs[self.nid]['halt']
        if reqs[self.nid]['halt']:
            raise EOFError
        if self.nid == 0 and idle:
            r = special_package[0]
            reqs[self.nid]['inputs'].append(special_package[1])
            if special_package[1] in sent:
                print(special_package[1])
                sent = None
            else:
                sent.add(special_package[1])
            return r
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
                special_package = self.input[1], self.input[2]
                self.input.clear()
                raise EOFError
            reqs[self.input[0]]['inputs'].append(self.input[1])
            reqs[self.input[0]]['inputs'].append(self.input[2])
            self.input.clear()


network = []

for i in range(50):
    reqs[i] = {}
    reqs[i]['halt'] = False
    reqs[i]['inputs'] = [i]

    network.append(Part23a(prompt.copy(), i))

idlecount = 0

while sent is not None:
    cycleidle = True
    for ic in network:
        ic.run()
        ic.input.clear()
        for i in range(50):
            cycleidle = cycleidle and len(reqs[i]['inputs']) == 0

    if cycleidle:
        idlecount += 1
    else:
        idlecount = 0
    if idlecount > 4:
        idle = True
    else:
        idle = False

with open('Q9.txt', 'r') as op:
    prompt = op.read()

prompt = prompt.strip()
prompt = prompt.split(',')

prompt = list(map(int, prompt))


def run(codes, start, inp, base):

    skip = 0
    for i in range(start, len(codes)):
        if skip > 0:
            skip -= 1
            continue

        k = str(codes[i])

        while len(k) < 5:
            k = "0" + k

        p = int(k[1])
        q = int(k[2])
        m = int(k[0])
        op = int(k[3:])

        if op == 1:
            codes[i + 3 if m == 1 else codes[i + 3] + base if m == 2 else codes[i + 3]] = codes[i + 1 if q == 1 else codes[i + 1] + base if q == 2 else codes[i + 1]] + codes[i + 2 if p == 1else codes[i + 2] + base if p == 2 else codes[i + 2]]
            skip = 3
        elif op == 2:
            codes[i + 3 if m == 1 else codes[i + 3] + base if m == 2 else codes[i + 3]] = codes[i + 1 if q == 1 else codes[i + 1] + base if q == 2 else codes[i + 1]]  * codes[i + 2 if p == 1 else codes[i + 2] + base if p == 2 else codes[i + 2]]
            skip = 3
        elif op == 3:
            codes[i + 1 if q == 1 else codes[i + 1] + base if q == 2 else codes[i + 1]] = inp
            skip = 1
        elif op == 4:
            return codes[i + 1 if q == 1 else codes[i + 1] + base if q == 2 else codes[i + 1]]
        elif op == 5:
            if codes[i + 1 if q == 1 else codes[i + 1] + base if q == 2 else codes[i + 1]] != 0:
                return run(codes, codes[i + 2 if p == 1 else codes[i + 2] + base if p == 2 else codes[i + 2]], inp, base)
            skip = 2
        elif op == 6:
            if codes[i + 1 if q == 1 else codes[i + 1] + base if q == 2 else codes[i + 1]] == 0:
                return run(codes, codes[i + 2 if p == 1 else codes[i + 2] + base if p == 2 else codes[i + 2]], inp, base)
            skip = 2
        elif op == 7:
            codes[i + 3 if m == 1 else codes[i + 3] + base if m == 2 else codes[i + 3]] = 1 if codes[i + 1 if q == 1 else codes[i + 1] + base if q == 2 else codes[i + 1]]  < codes[i + 2 if p == 1 else codes[i + 2] + base if p == 2 else codes[i + 2]] else 0
            skip = 3
        elif op == 8:
            codes[i + 3 if m == 1 else codes[i + 3] + base if m == 2 else codes[i + 3]] = 1 if codes[i + 1 if q == 1 else codes[i + 1] + base if q == 2 else codes[i + 1]] == codes[i + 2 if p == 1 else codes[i + 2] + base if p == 2 else codes[i + 2]] else 0
            skip = 3
        elif op == 9:
            base += codes[i + 1 if q == 1 else codes[i + 1] + base if q == 2 else codes[i + 1]]
            skip = 1
        else:
            print(k)
            assert False

try:
    print(run(prompt, 0, 1, 0))
except IndexError:
    print(run(prompt+[0]*len(prompt), 0, 1, 0))


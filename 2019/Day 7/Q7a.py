from itertools import permutations

with open('Q7.txt', 'r') as op:
    prompt = op.read()

prompt = prompt.strip()
prompt = prompt.split(',')

prompt = list(map(int, prompt))


def run(codes, start, inp, nxt=None):

    skip = 0
    for i in range(start, len(codes)):
        if skip > 0:
            skip -= 1
            continue

        k = str(codes[i])

        while len(k) < 4:
            k = "0" + k

        p = int(k[0])
        q = int(k[1])
        op = int(k[2:])

        if op == 1:
            codes[codes[i + 3]] = codes[i + 1 if q else codes[i + 1]] + codes[i + 2 if p else codes[i + 2]]
            skip = 3
        elif op == 2:
            codes[codes[i + 3]] = codes[i + 1 if q else codes[i + 1]] * codes[i + 2 if p else codes[i + 2]]
            skip = 3
        elif op == 3:
            codes[codes[i + 1]] = inp
            if next is not None:
                inp = nxt
                nxt = None
            skip = 1
        elif op == 4:
            return codes[i + 1 if q else codes[i + 1]]
        elif op == 5:
            if codes[i + 1 if q else codes[i + 1]] != 0:
                return run(codes, codes[i + 2 if p else codes[i + 2]], inp)
            skip = 2
        elif op == 6:
            if codes[i + 1 if q else codes[i + 1]] == 0:
                return run(codes, codes[i + 2 if p else codes[i + 2]], inp)
            skip = 2
        elif op == 7:
            codes[codes[i + 3]] = 1 if codes[i + 1 if q else codes[i + 1]] < codes[i + 2 if p else codes[i + 2]] else 0
            skip = 3
        elif op == 8:
            codes[codes[i + 3]] = 1 if codes[i + 1 if q else codes[i + 1]] == codes[i + 2 if p else codes[i + 2]] else 0
            skip = 3
        else:
            print(k)
            assert False


ans = None

trials = list(permutations([0, 1, 2, 3, 4]))

for i in trials:
    codes = prompt.copy()
    inp = 0
    for j in i:
        inp = run(codes, 0, j, inp)
    ans = inp if ans is None else max(ans, inp)

print(ans)
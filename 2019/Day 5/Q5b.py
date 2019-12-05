with open('Q5.txt', 'r') as f:
    prompt = f.read()

prompt = prompt.strip()
prompt = prompt.split(',')

prompt = list(map(int, prompt))

inp = 5


def run(codes, start):

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
            skip = 1
        elif op == 4:
            return codes[i + 1 if q else codes[i + 1]]
        elif op == 5:
            if codes[i + 1 if q else codes[i + 1]] != 0:
                return run(codes, codes[i + 2 if p else codes[i + 2]])
            skip = 2
        elif op == 6:
            if codes[i + 1 if q else codes[i + 1]] == 0:
                return run(codes, codes[i + 2 if p else codes[i + 2]])
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


print(run(prompt, 0))


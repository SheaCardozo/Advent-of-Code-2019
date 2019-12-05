with open('Q5.txt', 'r') as op:
    prompt = op.read()

prompt = prompt.strip()
prompt = prompt.split(',')

prompt = list(map(int, prompt))

inp = 1

skip = 0
for i in range(0, len(prompt)):
    if skip > 0:
        skip -= 1
        continue

    k = str(prompt[i])

    while len(k) < 4:
        k = "0" + k

    p = int(k[0])
    q = int(k[1])
    op = int(k[2:])

    if op == 1:
        prompt[prompt[i + 3]] = prompt[i + 1 if q else prompt[i + 1]] + prompt[i + 2 if p else prompt[i + 2]]
        skip = 3
    elif op == 2:
        prompt[prompt[i + 3]] = prompt[i + 1 if q else prompt[i + 1]] * prompt[i + 2 if p else prompt[i + 2]]
        skip = 3
    elif op == 3:
        prompt[prompt[i + 1]] = inp
        skip = 1
    elif op == 4:
        print(prompt[i + 1 if q else prompt[i + 1]])
        skip = 1
    else:
        assert op == 99
        break

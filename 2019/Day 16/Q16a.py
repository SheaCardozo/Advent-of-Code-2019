with open('Q16.txt', 'r') as op:
    prompt = op.read()

signal = [int(x) for x in prompt.strip()]
pattern = [0, 1, 0, -1]

for phase in range(100):
    new = signal.copy()
    for i in range(len(new)):
        val = 0
        count = 1
        for k in signal:
            val += k * pattern[(count // (i + 1)) % len(pattern)]
            count += 1
        new[i] = int(str(val)[-1])
    signal = new

print("".join(list(map(str, signal))))

with open('Q16.txt', 'r') as op:
    prompt = op.read()

signal = [int(x) for x in prompt.strip()]
signal = signal * 10000
offset = int(prompt[:7])
signal = signal[offset:]
for phase in range(100):
    for i in range(len(signal) - 1, 0, -1):
        signal[i - 1] = (signal[i] + signal[i - 1]) % 10

print("".join(list(map(str, signal[:8]))))

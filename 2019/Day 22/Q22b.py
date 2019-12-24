with open('Q22.txt', 'r') as f:
    prompt = f.read()

prompt = prompt.strip()
prompt = prompt.split('\n')

deck_len = 119315717514047
repeat = 101741582076661
track = 2020

a = 1
b = 0

for i in prompt:
    if i == 'deal into new stack':
        a *= -1
        b += a
    elif i[:3] == 'cut':
        b += int(i.split(' ')[-1]) * a
    elif i[:19] == 'deal with increment':
        a *= pow(int(i.split(' ')[-1]), -1, deck_len)
    else:
        assert False

track = (track * pow(a, repeat, deck_len) + b * (1 - pow(a, repeat, deck_len)) * pow(1 - a, -1, deck_len)) % deck_len

print(track)


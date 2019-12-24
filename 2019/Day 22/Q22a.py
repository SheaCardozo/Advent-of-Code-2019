with open('Q22.txt', 'r') as f:
    prompt = f.read()

prompt = prompt.strip()
prompt = prompt.split('\n')

deck = []


def cut_deck(deck, n):
    deck = deck[n:] + deck[:n]
    return deck


def mod_deal(deck, n):
    ans = [0] * len(deck)
    ind = 0

    for i in deck:
        ans[ind] = i
        ind = (ind + n) % len(deck)

    return ans


for i in range(10007):
    deck.append(i)

for i in prompt:
    if i == 'deal into new stack':
        deck.reverse()
    elif i[:3] == 'cut':
        deck = cut_deck(deck, int(i.split(' ')[-1]))
    elif i[:19] == 'deal with increment':
        deck = mod_deal(deck, int(i.split(' ')[-1]))
    else:
        assert False

for i, k in enumerate(deck):
    if k == 2019:
        print(i)


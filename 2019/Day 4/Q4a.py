a = 278384
b = 824795

ans = set()

for i in range(a, b + 1):
    if len(str(i)) != 6:
        continue

    last = None
    valid = False

    for p in str(i):
        if last is not None:
            if int(p) < int(last):
                valid = False
                break
            if p == last:
                valid = True

        last = p

    if valid:
        ans.add(i)

print(len(ans))

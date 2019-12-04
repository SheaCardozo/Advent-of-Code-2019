a = 278384
b = 824795

ans = set()

for i in range(a, b + 1):
    if len(str(i)) != 6:
        continue

    last = None
    groups = []

    for p in str(i):
        if last is not None:
            if int(p) < int(last):
                groups.clear()
                break
            if p == last:
                groups[-1] = groups[-1] + p
            else:
                groups.append(p)
        else:
            groups.append(p)

        last = p

    valid = False

    for q in groups:
        if len(q) == 2:
            valid = True

    if valid:
        ans.add(i)

print(len(ans))

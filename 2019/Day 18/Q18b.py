with open('Q18b.txt', 'r') as f:
    prompt = f.read()

prompt = prompt.split()

grid = []
starts = []

for i in prompt:
    grid.append([])
    for j in i:
        grid[-1].append(j)

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == '@':
            starts.append((i,j))


def find_keys(pos, grid, found):
    points = [pos]
    dist = {pos: 0}
    keys = {}

    while len(points) > 0:
        check = points[0]
        points = points[1:]
        for p in (
            (check[0] + 1, check[1]),
            (check[0] - 1, check[1]),
            (check[0], check[1] + 1),
            (check[0], check[1] - 1),
        ):
            if not (0 <= p[0] < len(grid) and 0 <= p[1] < len(grid[0])):
                continue
            c = grid[p[0]][p[1]]
            if c == '#':
                continue
            if p in dist:
                continue
            dist[p] = dist[check] + 1
            if 'A' <= c <= 'Z' and c.lower() not in found:
                continue
            if 'a' <= c <= 'z' and c not in found:
                keys[c] = dist[p], p
            else:
                points.append(p)
    return keys


def reachable4(grid, starts, havekeys):
    keys = {}
    for i, start in enumerate(starts):
        for ch, (dist, pt) in find_keys(start, grid, havekeys).items():
            keys[ch] = dist, pt, i
    return keys


def minwalk(grid, starts, found):
    hks = ''.join(sorted(found))
    if (starts, hks) in seen:
        return seen[starts, hks]
    keys = reachable4(grid, starts, found)
    if len(keys) == 0:
        ans = 0
    else:
        poss = []
        for ch, (dist, pt, roi) in keys.items():
            nstarts = tuple(pt if i == roi else p for i, p in enumerate(starts))
            poss.append(dist + minwalk(grid, nstarts, found + ch))
        ans = min(poss)
    seen[starts, hks] = ans
    return ans


seen = {}

print(minwalk(grid, tuple(starts), ''))

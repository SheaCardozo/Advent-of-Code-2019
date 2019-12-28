with open('Q20.txt', 'r') as f:
    prompt = f.read()

prompt = prompt.split('\n')

grid = []
current = 0, 0, 0
warps = {}

for i in prompt:
    grid.append([])
    for j in i:
        grid[-1].append(j)

grid = grid[:-1]


def find_warp(pos, grid):
    if grid[pos[0] + 1][pos[1]] not in (' ', '.', '#'):
        return grid[pos[0] + 1][pos[1]] + grid[pos[0] + 2][pos[1]]
    elif grid[pos[0] - 1][pos[1]] not in (' ', '.', '#'):
        return grid[pos[0] - 2][pos[1]] + grid[pos[0] - 1][pos[1]]
    elif grid[pos[0]][pos[1] + 1] not in (' ', '.', '#'):
        return grid[pos[0]][pos[1] + 1] + grid[pos[0]][pos[1] + 2]
    elif grid[pos[0]][pos[1] - 1] not in (' ', '.', '#'):
        return grid[pos[0]][pos[1] - 2] + grid[pos[0]][pos[1] - 1]
    else:
        return None


for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == '.':
            d = find_warp((i, j), grid)
            if d is not None:
                warps[i, j] = d

for i in warps:
    if warps[i] == 'AA':
        current = i[0], i[1], 0
    if warps[i] == 'ZZ':
        goal = i[0], i[1], 0

warps.pop((current[0], current[1]))
warps.pop((goal[0], goal[1]))


def find_path(pos, grid):
    points = [pos]
    dist = {pos: 0}

    while len(points) > 0:
        if goal in dist:
            return dist[goal]
        check = points[0]
        points = points[1:]
        if (check[0], check[1]) in warps:
            for i in warps:
                if i != (check[0], check[1]) and warps[i] == warps[(check[0], check[1])]:
                    if 96 >= check[0] >= 36 and 96 >= check[1] >= 36:
                        z = check[2] + 1
                        if (i[0], i[1], z) not in dist:
                            dist[i[0], i[1], z] = dist[check] + 1
                            points.append((i[0], i[1], z))
                    else:
                        z = check[2] - 1
                        if (i[0], i[1], z) not in dist and z >= 0:
                            dist[i[0], i[1], z] = dist[check] + 1
                            points.append((i[0], i[1], z))

        for p in (
            (check[0] + 1, check[1], check[2]),
            (check[0] - 1, check[1], check[2]),
            (check[0], check[1] + 1, check[2]),
            (check[0], check[1] - 1, check[2]),
        ):
            if not (0 <= p[0] < len(grid) and 0 <= p[1] < len(grid[0])):
                continue
            c = grid[p[0]][p[1]]
            if c != '.':
                continue
            if p in dist:
                continue
            dist[p] = dist[check] + 1
            points.append(p)


print(find_path(current, grid))

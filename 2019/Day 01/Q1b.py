from utils import puzzle_input

inp = map(int, puzzle_input('Q1.txt'))


def req_fuel(i):
    return min(0, i) or i + req_fuel(i//3 - 2)


print(sum(map(lambda x: req_fuel(x//3 - 2), inp)))

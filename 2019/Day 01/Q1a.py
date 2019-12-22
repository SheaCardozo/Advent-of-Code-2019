from utils import puzzle_input

inp = map(int, puzzle_input('Q1.txt'))

print(sum(map(lambda x: x//3 - 2, inp)))

def puzzle_input(path):
    with open(path, 'r') as f:
        prompt = f.read()

    return prompt.split()

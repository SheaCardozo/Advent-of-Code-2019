with open('Q2.txt', 'r') as f:
    prompt = f.read()

prompt = prompt.strip()
prompt = prompt.split(',')

prompt = list(map(int, prompt))

for i in range(0, len(prompt), 4):
    if prompt[i] == 1:
        prompt[prompt[i + 3]] = prompt[prompt[i + 1]] + prompt[prompt[i + 2]]
    elif prompt[i] == 2:
        prompt[prompt[i + 3]] = prompt[prompt[i + 1]] * prompt[prompt[i + 2]]
    else:
        assert prompt[i] == 99
        break

print(prompt[0])

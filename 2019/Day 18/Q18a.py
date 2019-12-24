with open('Q18.txt', 'r') as f:
    prompt = f.read()

prompt = prompt.split()

for x in prompt:
    print(x)
with open('Q8.txt', 'r') as op:
    prompt = op.read()

prompt = prompt.strip()
layers = []
for i in range(0, len(prompt), 150):
    layer = prompt[i:i+150]
    layers.append(layer)

image = ""

for i in range(150):
    for layer in layers:
        if layer[i] != '2':
            image += layer[i]
            break

for j in range(6):
    print(image[j*25: (j+1)*25].replace('0', ' '))

# Printed answer is FHJUL

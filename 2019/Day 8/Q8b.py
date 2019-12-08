with open('Q8.txt', 'r') as op:
    prompt = op.read()

prompt = prompt.strip()
layers = []
for i in range(0, len(prompt), 150):

    layer = [0] * 150

    for k, j in enumerate(prompt[i:i+150]):
        layer[k] = int(j)

    layers.append(layer)

image = [0] * 150

for i in range(150):
    for layer in layers:
        if layer[i] == 2:
            continue
        else:
            image[i] = layer[i]
            break

for j in range(6):
    print(image[j*25: (j+1)*25])
    print('\n')

#Printed answer is FHJUL
from utils import puzzle_input

with open('Q2.txt', 'r') as f:
    prompt = f.read()

prompt = prompt.strip()
prompt = prompt.split(',')

prompt = list(map(int, prompt))

backup = prompt.copy()


def run_sequence(seq):

    for i in range(0, len(seq), 4):

        if seq[i] == 99:
            break
        elif seq[i] == 1:
            seq[seq[i + 3]] = seq[seq[i + 1]] + seq[seq[i + 2]]
        elif prompt[i] == 2:
            seq[seq[i + 3]] = seq[seq[i + 1]] * seq[seq[i + 2]]
        else:
            print('error')

    return seq


for p in range(0, 99):
    for q in range(0, 99):
        prompt = backup.copy()
        prompt[1] = p
        prompt[2] = q

        prompt = run_sequence(prompt)

        if prompt[0] == 19690720:
            print(p*100 + q)
            break


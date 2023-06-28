import random

for _ in range(20):
    line = '[' + ' '.join([f'{random.uniform(0, 1):.3f}' for _ in range(2)]) + ' ... ' + ' '.join([f'{random.uniform(0, 1):.3f}' for _ in range(2)]) + ']'
    print(line)
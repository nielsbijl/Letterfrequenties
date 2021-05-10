import numpy as np

nl_matrix = np.load('nlmatrix.npy')
en_matrix = np.load('enmatrix.npy')

allowed_chars = 'abcdefghijklmnopqrstuvwxyz *'
clean_input = []

with open('validation.txt', 'r', encoding='utf-8') as nltext:
    lines = nltext.readlines()
    print(lines)
    for line in lines:
        clean_input.append(line.replace('\n', ''))

print(clean_input)
split_input = []
for line in clean_input:
    split_input.append(line.lstrip().lower())


nl_count = 0
en_count = 0
for line in split_input:
    if line:
        matrix = np.zeros((28, 28))
        chars = list(map(lambda x: x if x in allowed_chars else '*', line))
        for i in range(len(chars)-1):
            matrix[allowed_chars.index(chars[i]), allowed_chars.index(chars[i+1])] += 1
        nl_score = np.sum(np.abs(nl_matrix - matrix))
        en_score = np.sum(np.abs(en_matrix - matrix))
        if nl_score > en_score:
            en_count += 1
        else:
            nl_count += 1
print(nl_count, en_count)
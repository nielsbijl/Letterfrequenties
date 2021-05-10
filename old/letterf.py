import numpy as np

matrix = np.zeros((28, 28))
allowed_chars = 'abcdefghijklmnopqrstuvwxyz *'
clean_input = []

with open('entext.txt', 'r', encoding='utf-8') as nltext:
    lines = nltext.readlines()
    print(lines)
    for line in lines:
        clean_input.append(line.replace('\n', ''))

print(clean_input)
split_input = []
for line in clean_input:
    split_input.append(line.lstrip().lower())


matrices = []
for line in split_input:
    if line:
        tmp_matrix = np.zeros((28, 28))
        chars = list(map(lambda x: x if x in allowed_chars else '*', line))
        for i in range(len(chars)-1):
            tmp_matrix[allowed_chars.index(chars[i]), allowed_chars.index(chars[i+1])] += 1
        matrices.append(tmp_matrix)
matrix = np.average(matrices, axis=0)
print(matrix)
np.save('enmatrix', matrix)
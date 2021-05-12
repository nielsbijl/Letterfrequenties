import sys
from itertools import groupby
import numpy as np

lang = sys.argv[1]

allowed_chars = 'abcdefghijklmnopqrstuvwxyz *'
matrix = np.zeros((28, 28))
for line in sys.stdin:
    data = line.rstrip('\n').split('\t')
    matrix[allowed_chars.index(data[0][0]), allowed_chars.index(data[0][1])] = data[1]
matrix = matrix / matrix.sum(axis=1)[:, None]
print(matrix)
np.save(f'{lang}_fit', matrix)

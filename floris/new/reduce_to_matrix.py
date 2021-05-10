import sys
from itertools import groupby
import numpy as np

data = [line.rstrip('\n').split('\t') for line in sys.stdin]
allowed_chars = 'abcdefghijklmnopqrstuvwxyz *'
for chars, group in groupby(data, lambda x: x[0]):
    matrix = np.zeros((28, 28))
    for i in group:
        matrix[allowed_chars.index(i[1][0]), allowed_chars.index(i[1][1])] = i[2]
    print(f'{chars}\t{matrix.tobytes()}')
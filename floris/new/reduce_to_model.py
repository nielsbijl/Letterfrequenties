import sys
import numpy as np

matrices_raw = [line.rstrip('\n').split('\t')[1] for line in sys.stdin]
matrices = []
for matrix in matrices_raw:
    matrices.append(np.frombuffer(matrix).reshape((28,28)))
print(matrices[0])
matrix = np.average(matrices, axis=0)
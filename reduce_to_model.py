import ast
import sys
import numpy as np

lang = sys.argv[1]
matrices_raw = [line.rstrip('\n').split('\t')[1] for line in sys.stdin]
matrices = []
# We read all the matrices
for matrix in matrices_raw:
    matrix = ast.literal_eval(matrix)
    matrices.append(np.frombuffer(matrix).reshape((28, 28)))
# Take the average of each matrix to create a model.
matrix = np.average(matrices, axis=0)
print(matrix)
np.save(f'{lang}_fit', matrix)

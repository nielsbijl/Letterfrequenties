import sys
import ast
from itertools import groupby
import numpy as np

classes = {'en': np.load(sys.argv[1]), 'nl': np.load(sys.argv[2])}
classes_count = {'en': 0, 'nl': 0}

for line in sys.stdin:
    matrix_raw = line.rstrip('\n').split('\t')[1]
    matrix = ast.literal_eval(matrix_raw)
    matrix = np.frombuffer(matrix).reshape((28, 28))
    min_score = np.inf
    min_class = ''
    for i in classes.keys():
        score = np.sum(np.abs(classes[i] - matrix))
        if score < min_score:
            min_score = score
            min_class = i
    classes_count[min_class] += 1
    # print(min_class)
print(classes_count)
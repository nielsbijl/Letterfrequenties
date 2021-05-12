import sys
from itertools import groupby

data = [line.rstrip('\n').split('\t') for line in sys.stdin]
# Group by letter combinations
for chars, group in groupby(data, lambda x: x[0]):
    print(f'{chars}\t{len(list(group))}')

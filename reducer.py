import sys
from itertools import groupby

data = [line.rstrip('\n').split('\t') for line in sys.stdin]
# First group per line number.
for chars, group in groupby(data, lambda x: x[0]):
    # Then group by letter combination.
    for inner_chars, inner_group in groupby(group, lambda x: x[1]):
        print(f'{chars}\t{inner_chars}\t{len(list(inner_group))}')

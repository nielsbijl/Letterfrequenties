import sys
from itertools import groupby

if __name__ == "__main__":
    data = [line.rstrip('\n').split('\t', 1) for line in sys.stdin]

    for chars, group in groupby(data, lambda x: x[0]):
        group = list(group)
        print("{}\t{}".format(chars, len(group)))

"""
RUN: mapper.py < text.txt | sort | reduce.py

"""
import sys
from itertools import groupby

if __name__ == "__main__":
    sep = '\t'
    data = [line.rstrip('\n').split(sep, 1) for line in sys.stdin]

    for chars, group in groupby(data, lambda x: x[0]):
        group = list(group)
        print("{}{}{}".format(chars, sep, len(group)))

"""
RUN: mapper.py < text.txt | sort | reduce.py

"""

import sys

current_chars = None
current_count = 0
chars = None

lines = sys.stdin.readlines()
lines.sort()

for line in lines:
    line = line.strip()

    chars, count = line.split('\t', 1)
    count = int(count)

    if current_chars == chars:
        current_count += count
    else:
        if current_chars:
            print('%s\t%s' % (current_chars, current_count))
        current_count = count
        current_chars = chars

if current_chars == chars:
    print('%s\t%s' % (current_chars, current_count))


"""
RUN: reduce.py < mapoutput.txt
"""
import sys
import os
import numpy as np
import time

c = 0
for line in sys.stdin.readlines():
    allowed_chars = 'abcdefghijklmnopqrstuvwxyz *'
    line_input = line.replace('\n', '').lower()
    if line_input:
        chars = list(map(lambda x: x if x in allowed_chars else '*', line_input))
        for i in range(len(chars) - 1):
            print(f'{c}\t{chars[i]}{chars[i+1]}\t1')
        c += 1


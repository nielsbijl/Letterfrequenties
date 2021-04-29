import sys

string = sys.stdin.read()

allowed_chars = 'abcdefghijklmnopqrstuvwxyz '

for index in range(len(string)):
    if index < len(string) - 1:
        char0 = string[index]
        if char0 not in allowed_chars:
            char0 = '_'
        char1 = string[index + 1]
        if char1 not in allowed_chars:
            char1 = '_'

        print('%s\t%s' % (char0 + char1, 1))



"""
RUN: mapper.py < text.txt > mapoutput.txt

run mapper.py with text.txt as stdin and write stdout to mapoutput.txt

RUN ALL: mapper.py < text.txt | reduce.py
"""
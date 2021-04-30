import sys


if __name__ == "__main__":
    text = sys.stdin.read()

    allowed_chars = 'abcdefghijklmnopqrstuvwxyz '

    chars = list(map(lambda x: x if x in allowed_chars else '_', text))

    for index in range(len(chars)):
        if index < len(chars) - 1:
            char0 = chars[index]
            char1 = chars[index + 1]
            print('%s\t%s' % (char0 + char1, 1))



"""
RUN: mapper.py < text.txt > mapoutput.txt

run mapper.py with text.txt as stdin and write stdout to mapoutput.txt

RUN ALL: mapper.py < text.txt | reduce.py
"""

import sys

# For each row in a text file.
for line in sys.stdin:
    allowed_chars = 'abcdefghijklmnopqrstuvwxyz *'
    line_input = line.replace('\n', '').lower()
    if line_input:
        # Replace the chars in each line with the allowed chars.
        chars = list(map(lambda x: x if x in allowed_chars else '*', line_input))
        for i in range(len(chars) - 1):
            # Print all the letter combinations.
            print(f'{chars[i]}{chars[i+1]}\t1')

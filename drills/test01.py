import sys

text = sys.stdin.read().strip()

for i in range(len(text)-1, -1, -1):
    print(text[i], end="")
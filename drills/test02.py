import sys

text = sys.stdin.read().strip()

if text == text[::-1]:
        print("ano")
else:
        print("nie")





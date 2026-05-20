import sysd

slova = sys.stdin.read().strip()
stack = []
pary = {')':'(', '}':'{', ']':'['}

for znak in slova:
    if znak in '({[':
        stack.append(znak)
    elif znak in ']})':
        if not stack or stack[-1] != pary[znak]:
            print("nie")
            exit()
        stack.pop()
if stack:
    print("nie")
else:
    print("ano")







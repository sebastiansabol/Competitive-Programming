n = input()
counter = 0
for ch in n:
    if ch in ("4", "7"):
        counter += 1
if counter in (4, 7):
    print("YES")
else:
    print("NO")

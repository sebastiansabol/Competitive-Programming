import sys 

k = int(input())
pisomky = list(map(int, sys.stdin.read().split()))
pocitadlo = {}

for x in pisomky:
    pocitadlo[x] = pocitadlo.get(x, 0)+1
    if pocitadlo[x] <= k:
        result.append(x)
    else:
        print(*pocitadlo)


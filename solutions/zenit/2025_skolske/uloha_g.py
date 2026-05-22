import sys

k = int(input())
pisomky = list(map(int, sys.stdin.read().split()))
pocitadlo = {}
result = []

for x in pisomky:
    pocitadlo[x] = pocitadlo.get(x, 0) + 1
    if pocitadlo[x] <= k:
        result.append(x)

print(*result)

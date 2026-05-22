import sys

n = int(input())
cisla = list(map(int, input().split()))
cisla.sort()
rozdiel = cisla[-1] - cisla[0]

# Najvacsi sucin
if cisla[-1] * cisla[-2] >= cisla[0] * cisla[1]:
    a, b = sorted([cisla[-1], cisla[-2]])
else:
    a, b = sorted([cisla[0], cisla[1]])
print(a, b)

# Najmensi sucin
if cisla[0] * cisla[-1] <= cisla[1] * cisla[-1]:
    a, b = sorted([cisla[0], cisla[-1]])
else:
    a, b = sorted([cisla[1], cisla[-1]])
print(a, b)

# Najvacsi podiel
a, b = sorted([cisla[-1], cisla[-2]])
print(b, a)

# Najmensi podiel
a, b = sorted([cisla[-1], cisla[0]])
print(b, a)
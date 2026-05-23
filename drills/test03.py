import sys

cisla = list(map(int, input().split()))
maximum = max(cisla)
idx = cisla.index(maximum)
print(maximum, idx)
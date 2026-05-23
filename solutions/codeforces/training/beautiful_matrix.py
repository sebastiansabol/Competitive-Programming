import sys

matrix = []
for i in range(5):
    riadok = list(map(int, input().split()))
    matrix.append(riadok)
for i, riadok in enumerate(matrix):
    for j, hodnota in enumerate(riadok):
        if hodnota == 1:
            print(abs(i-2) + abs(j-2))


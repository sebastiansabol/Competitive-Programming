n = int(input())
line_result = []
for i in range(n):
        a, b = map(int,input().split())
        vysledok = b - a
        line_result.append(vysledok)
current = 0
maximum = 0
for vysledok in line_result:
    current += vysledok
    if current > maximum:
        maximum = current
print(maximum)

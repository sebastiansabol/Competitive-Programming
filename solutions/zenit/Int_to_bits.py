n = int(input())
for i in range(n):
        x = int(input())
        s = format(x, '032b')
        s = s[::-1]
        vysledok = int(s, 2)
        print(vysledok)

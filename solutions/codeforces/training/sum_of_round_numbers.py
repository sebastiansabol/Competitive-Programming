n = int(input())
for _ in range(n):
        s = input()
        vysledky = []
        for i, znak in enumerate(s):
                if znak != "0":
                        vysledky.append(int(znak) * 10 ** (len(s) - 1 - i))
        print(len(vysledky))
        print(*vysledky)

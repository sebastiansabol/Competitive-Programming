k = int(input())
for i in range(k):
        found = False
        n = int(input())
        for a in range(n//3 + 1):
                for b in range(n//7 + 1):
                        for c in range(n//11 + 1):
                                if 3*a + 7*b + 11*c == n:
                                        found = True
        print("ANO" if found else "NIE")

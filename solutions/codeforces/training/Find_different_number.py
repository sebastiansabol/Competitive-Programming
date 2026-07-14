n = int(input())
for _ in range(n):
        s = int(input())
        g = list(map(int, input().split()))
        d = {}
        for znak in g:
                if znak in d:
                        d[znak] += 1
                else:
                        d[znak] = 1
        for numbers in d:
                if d[numbers] == 1:
                        spy = numbers
        print(g.index(spy) + 1)
        

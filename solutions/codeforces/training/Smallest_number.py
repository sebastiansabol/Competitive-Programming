t = int(input())
for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        normal = sorted(a)
        ok = False
        for i in range(len(normal) - 1):
                if (normal[i+1] - normal[i]) > 1:
                        ok = True
        if ok:
                print("NO")
        else:
                print("YES")
                        
        

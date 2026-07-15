n, k = map(int, input().split())
if k == 100:
    print(-1)
else:
    print(n * 100 / (100 - k))

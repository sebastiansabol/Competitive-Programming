n = int(input())
counter = 0
for i in range(n):
        a, b = list(map(int, input().split()))
        if a % b != 0:
                print( b - (a%b))
        elif a % b == 0:
                print(0)

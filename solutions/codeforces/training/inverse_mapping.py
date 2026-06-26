n = int(input())
p = list(map(int, input().split()))
final = [0] * n 
for i in range(n):
     final[p[i] - 1] = i + 1
print(*final)
        

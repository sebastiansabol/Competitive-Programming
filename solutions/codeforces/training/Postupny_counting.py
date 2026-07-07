n, k = map(int,input().split())
total = 0
count = 0
for i in range(1, n+1):
        if total + ((5*i) + k) <= 240:
                total += 5*i
                count+=1
print(count)
    

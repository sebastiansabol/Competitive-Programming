n = int(input())
s = list(map(int, input().split()))
max_val = s[0]
min_val = s[0]
counter = 0
for i in range(1, n):
        if s[i] > max_val:
                max_val = s[i]
                counter +=1
        elif s[i] < min_val:
                min_val = s[i]
                counter +=1
print(counter)
        
        
        

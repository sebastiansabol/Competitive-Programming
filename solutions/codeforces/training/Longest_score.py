n = int(input())
for _ in range(n):
        s = int(input())
        a = list(map(int, input().split()))
        score = 0
        maximum = 0
        for i in a:
                if i == 1:
                        maximum = max(maximum, score)
                        score = 0
                elif i == 0:
                        score += 1
        maximum = max(maximum, score)
        print(maximum)
                        
                
                
                        
                

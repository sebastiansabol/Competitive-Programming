n = int(input())
s = map(int, input().split())
policeman = 0
occured = 0
for i in s:
        if i > 0:
                policeman+=1
        elif i == -1 and policeman > 0:
                policeman -=1
        else:
                occured+=1
print(occured)
                
                

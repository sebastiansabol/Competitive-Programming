from ast import Continue


k = int(input())
cisla = list(map(int,input().split()))
count = {}

for x in cisla:
    count[x] = count.get(x, 0) + 1
    if count[x] > k:
        continue  
    else:
        print(x)




n = int(input())
ulohy = []
x = map(int, input().split())
y = map(int, input().split())
p = next(x) 
c = next(y)
for i in x:
    ulohy.append(i)
for k in y:
        ulohy.append(k)
if list(set(ulohy)) == list(range(1, n+1)):
        print("I become the guy.")
else:
        print("Oh, my keyboard!")

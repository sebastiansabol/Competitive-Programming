s = list(map(int, input().split()))
maximum = max(s)
s.remove(maximum)
list = []
for i in s:
        vysl = maximum - i
        list.append(vysl)
print(*list)

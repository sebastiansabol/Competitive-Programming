#Pattern: count integers 1..d divisible by at least one of k,l,m,n
# Key: range(1, d+1) — draci su 1-indexed, range je exclusive na konci
# Key: loop variable i v podmienke, nie d (fixna hodnota)
# Operator: % == 0 pre delitelnost, or pre "aspon jedna podmienka"

k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())
counter = 0
for i in range(1, d+1):
        if i % k == 0 or i % l == 0 or i % m == 0 or i % n == 0:
                counter+=1
                
print(counter)

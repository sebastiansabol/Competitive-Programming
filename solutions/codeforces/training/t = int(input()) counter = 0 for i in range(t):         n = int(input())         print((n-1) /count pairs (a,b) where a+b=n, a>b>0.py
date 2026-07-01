# CF 1426B - Candies and Two Sisters
# Pattern: count pairs (a,b) where a+b=n, a>b>0
# Math shortcut: b must be 1..floor(n/2)-exclusive → answer = (n-1)//2
# Key insight: when n is large (2e9), brute force is impossible → derive formula
t = int(input())
for i in range(t):
    n = int(input())
    print((n-1) // 2)

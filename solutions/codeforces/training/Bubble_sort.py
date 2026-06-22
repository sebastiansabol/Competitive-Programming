n, t = map(int,input().split())
s = list(input())
for _ in range(t):
        new = list(s)
        for i in range(n-1):
                if s[i] == "B" and s[i+1] == "G":
                        new[i] = "G"
                        new[i+1] = "B"
        s = new
print("".join(s))

n = int(input())
znaky = ""
for i in range(n):
    znaky += input()
if "<" in znaky or ">" in znaky:
    print("had")
else:
    print("dazdovka")

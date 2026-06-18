n = int(input())
anton = 0
danik = 0
for i in range(n):
        i = input()
        for char in i:
                if char == "A":
                        anton += 1
                elif char == "D":
                        danik += 1
if anton > danik:
        print("Anton")
elif danik > anton:
        print("Danik")
else:
        print("Friendship")

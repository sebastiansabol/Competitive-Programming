n = int(input())
cards = list(map(int, input().split()))
Sereja = 0
Dima = 0
left = 0
right = n-1
for turn in range(n):
        if cards[left] > cards[right]:
                picked = cards[left]
                left +=1
        else:
                picked = cards[right]
                right -= 1
        if turn % 2 == 0:
                Sereja += picked
        else:
                Dima += picked
print(Sereja, Dima)
                
                

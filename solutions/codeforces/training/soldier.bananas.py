k, n , w = map(int, input().split())
vysledky = []
for i in range(1,w+1):
      vysl = (i) * (k)
      vysledky.append(vysl)
s = sum(vysledky)
if s > n:
      final = s - n 
      print(final)
else:
      print(0)

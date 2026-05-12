import sys

# 1. Načítame všetko (N-ko aj počty cukríkov)
input_data = list(map(int, sys.stdin.read().split()))
n = input_data[0]
kopce = input_data[1:] # Od druhého čísla sú to naše kopy

# 2. Vytvoríme "priečinky" na čísla podľa zvyšku po delení 3
r0, r1, r2 = [], [], []

for k in kopce:
    if k % 3 == 0: r0.append(k)
    elif k % 3 == 1: r1.append(k)
    else: r2.append(k)

# 3. Logika: Stačí nám nájsť JEDNU platnú trojicu
if len(r0) >= 3:
    print(f"{r0[0]} {r0[1]} {r0[2]}")
elif len(r1) >= 3:
    print(f"{r1[0]} {r1[1]} {r1[2]}")
elif len(r2) >= 3:
    print(f"{r2[0]} {r2[1]} {r2[2]}")
elif len(r0) >= 1 and len(r1) >= 1 and len(r2) >= 1:
    print(f"{r0[0]} {r1[0]} {r2[0]}")

  

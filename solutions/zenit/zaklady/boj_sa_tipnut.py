import sys

# 1. Tvoj geniálny riadok (ten máš dobre!)
data = list(map(int, sys.stdin.read().split()))

# 2. Tu musíme použiť tú povinnú premennú 'clslo'
# Funkcia sum() zoberie tvoj list 'data' a sčíta ho
clslo = sum(data)

# 3. Vypíšeme výsledok (premennú, nie text!)
print(clslo + 1)

# Competitive Programming — Zenit 2026

## Počas súťaže — rýchla navigácia

| Čo hľadáš | Súbor |
|-----------|-------|
| Hash counter, dictionary | `drills/week01_hash_counter.py` |
| String search, split() | `solutions/zenit/2025_skolske/uloha_d.py` |
| Fast I/O (sys.stdin) | skopíruj: `import sys; input = sys.stdin.readline` |

## Vzory ktoré sa opakujú

**Counter pattern:**
```python
count = {}
count[x] = count.get(x, 0) + 1
```

**Split vstup — čísla:**
```python
cisla = list(map(int, input().split()))
```

**Split vstup — text:**
```python
import sys
slova = sys.stdin.read().split()
```

**Výstup listu:**
```python
print(*result)
```

## Progres
| Týždeň | Téma | Úloha |
|--------|------|-------|
| 1 | Hash counter | zenit25sk_g ✅ |
| 1 | String search | zenit25sk_d ✅ |

s = list(input().split())
final_male = []
final_velke = []
final_cisla = []
for i in s:
        male = []
        velke = []
        cisla = []
        for znak in i:
                if znak.isupper():
                        velke.append(znak)
                elif znak.islower() :
                        male.append(znak)
                elif znak.isdigit():
                        cisla.append(znak)
        final_male.append(male)
        final_velke.append(velke)
        final_cisla.append(cisla)
vysledok = []
for m in final_male:
    if m:
        vysledok.append("".join(m))
for v in final_velke:
    if v:
        vysledok.append("".join(v))
for c in final_cisla:
    if c:
        vysledok.append("".join(c))
print(" ".join(vysledok))
                        

slovo =input()
vycistene = slovo.replace("{","").replace("}","").replace(",","")
skoro = vycistene.split()
unique = set(skoro)
print(len(unique))
                

s = input()
counter_l =0
counter_h =0
for i in s:
           if i.isupper():
                      counter_h+=1
           else:
                      counter_l+=1
if counter_h > counter_l:
           print(s.upper())
else:
           print(s.lower())

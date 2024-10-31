quad_zahl = []

for k in range(1, 11):
    if k % 2 == 0:
        quad_zahl.append(k)
    else:
        quad_zahl.append(k**2)
        
print(quad_zahl)




quad_zahl_neu = [k**2 if k % 2 != 0 else k for k in range(1, 11)]

print(quad_zahl_neu)
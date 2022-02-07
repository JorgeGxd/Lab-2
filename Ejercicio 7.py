a = 0

for i in range(1001):
    
    if i % 7 == 0 and i != 0:
        a +=1

print(f"Multiplos solo con rango de un parametro : {a}")

a = 0
for i in range(7, 500, 7):
    if i % 7 == 0 and i != 0:
        a += 1

print(f"Multiplos con rango de tres parametro {a}")
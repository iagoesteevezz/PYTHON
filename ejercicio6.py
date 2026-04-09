num = int(input("Introduce un número:"))
cont = 0
for i in range(num**num):
    if num % i == 0:
        cont +=1
if cont > 2:
    print("El número no es primo")
else:
    print("El número es primo")
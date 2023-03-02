n = int(input("¿Cuántos números deseas sumar? "))
suma = 0.0

for i in range(n):
    num = float(input("Introduce el número {}: ".format(i+1)))
    suma += num

print("La suma total es: ", suma) #Hola

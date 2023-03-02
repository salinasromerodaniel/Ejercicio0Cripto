import fileinput

lines = []
for line in fileinput.input():
    lines.append(line)

suma = 0
for num in lines:
    suma += int(num)

print("La suma total es: ", suma)

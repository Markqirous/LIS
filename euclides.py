num1 = int(input("Introduce un número: "))
num2 = int(input("Introduce un número: "))

while num2 > 0:
    num1, num2 = num2, num1 % num2

print(num1)

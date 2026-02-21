def multiplicar_sumas(a,b):
    resultado = 0

    for i in range (b):
        resultado = resultado + a
    return resultado

num1 = int(input("ingrese el primer numero que desea multiplicar"))
num2 =int(input("ingrese el segundo numero que desea multiplicar"))
resultado = multiplicar_sumas(num1, num2)
print(f"El resultado de la multiplicación es: {resultado}")


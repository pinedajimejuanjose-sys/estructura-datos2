def multiplicar_recursion(a, b):
    if b == 0:
        return 0
    return a + multiplicar_recursion(a, b - 1)



def multiplicar_while(a, b):
    resultado = 0
    while b > 0:
        resultado = resultado + a
        b = b - 1
    return resultado


def multiplicar_for(a, b):
    resultado = 0
    for i in range(b):
        resultado = resultado + a
    return resultado



print(multiplicar_recursion(4, 3))  
print(multiplicar_recursion(7, 0))  
print(multiplicar_recursion(0, 9))  
print(multiplicar_recursion(6, 6))  
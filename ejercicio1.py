def suma_digitos(n):
    if n < 10:  # Caso base
        return n
    else:
        return (n % 10) + suma_digitos(n // 10)
    
 
def suma_digitos(n):
    suma = 0
    for digito in str(n):
        suma += int(digito)
    return suma

def suma_digitos(n):
    suma = 0
    while n > 0:
        suma += n % 10
        n //= 10
    return suma
def es_palindromo(texto):
  
    texto = texto.replace(" ", "")
    texto = texto.lower()

   
    if len(texto) == 0 or len(texto) == 1:
        return True

    if texto[0] != texto[-1]:
        return False

    
    return es_palindromo(texto[1:-1])



def es_palindromo_while(texto):
 
    texto = texto.replace(" ", "")
    texto = texto.lower()

    izquierda = 0
    derecha = len(texto) - 1

    while izquierda < derecha:
        if texto[izquierda] != texto[derecha]:
            return False
        izquierda = izquierda + 1
        derecha = derecha - 1

    return True



def es_palindromo_for(texto):
   
    texto = texto.replace(" ", "")
    texto = texto.lower()

    mitad = len(texto) // 2

    for i in range(mitad):
        if texto[i] != texto[-(i + 1)]:
            return False

    return True



print(es_palindromo("anita"))         
print(es_palindromo("racecar"))       
print(es_palindromo("python"))        
print(es_palindromo("A man a plan"))  

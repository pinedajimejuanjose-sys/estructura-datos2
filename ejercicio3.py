arr = [2, 5, 8, 12, 16, 23, 38, 45, 72, 91]


def busqueda_for(arr, objetivo):
    for i in range(len(arr)):
        if arr[i] == objetivo:
            return i
    return -1


def busqueda_while(arr, objetivo):
    izq, der = 0, len(arr) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if arr[medio] == objetivo:
            return medio
        elif objetivo < arr[medio]:
            der = medio - 1
        else:
            izq = medio + 1
    return -1


def busqueda_recursiva(arr, objetivo, izq, der):
    if izq > der:
        return -1
    medio = (izq + der) // 2
    if arr[medio] == objetivo:
        return medio
    elif objetivo < arr[medio]:
        return busqueda_recursiva(arr, objetivo, izq, medio - 1)
    else:
        return busqueda_recursiva(arr, objetivo, medio + 1, der)


print(busqueda_for(arr, 23))                        # → 5
print(busqueda_while(arr, 23))                      # → 5
print(busqueda_recursiva(arr, 23, 0, len(arr)-1))   # → 5
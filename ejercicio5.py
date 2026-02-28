def hanoi_recursion(n, origen, destino, auxiliar):
    if n == 0:
        return
    hanoi_recursion(n - 1, origen, auxiliar, destino)
    print("Mover disco", n, "de", origen, "a", destino)
    hanoi_recursion(n - 1, auxiliar, destino, origen)



def hanoi_while(n):
    pila = [(n, "A", "C", "B")]
    while len(pila) > 0:
        discos, origen, destino, auxiliar = pila.pop()
        if discos == 0:
            continue
        pila.append((discos - 1, auxiliar, destino, origen))
        print("Mover disco", discos, "de", origen, "a", destino)
        pila.append((discos - 1, origen, auxiliar, destino))


def hanoi_for(n):
    movimientos = []
    def generar(n, origen, destino, auxiliar):
        if n == 0:
            return
        generar(n - 1, origen, auxiliar, destino)
        movimientos.append((n, origen, destino))
        generar(n - 1, auxiliar, destino, origen)
    generar(n, "A", "C", "B")
    for disco, origen, destino in movimientos:
        print("Mover disco", disco, "de", origen, "a", destino)



print("=== RECURSIÓN ===")
hanoi_recursion(3, "A", "C", "B")

print("\n=== WHILE ===")
hanoi_while(3)

print("\n=== FOR ===")
hanoi_for(3)
def numeros_especiales(inicio: int, final: int, que_calculamos: str) -> int:
    suma = 0
    lista = []
    if que_calculamos == "pares":
        for numero in range(inicio, final):
            if numero % 3 == 0:
                continue
            if numero % 2 == 0:
                lista.append(numero)
            else:
                continue
    elif que_calculamos == "impares":
        for numero in range(inicio, final):
            if numero % 3 == 0:
                continue
            if numero % 2 == 1:
                lista.append(numero)
            else:
                continue
    for numero in lista:
        suma += numero
    return suma


if __name__ == '__main__':
    error = 0
    try:
        # Entrada
        inicio = int(input("Ingrese el número inicial \n(múltiplo de 10): "))
        final = int(input("Ingrese el número final \n(múltiplo de 10): "))
        if inicio % 10 != 0 or final % 10 != 0:
            raise ValueError
    except ValueError:
        # Salida
        error = 1
        print("Ingrese un número múltiplo de diez")
    try:
        if error == 1:
            raise ValueError
        # Entrada
        que_calculamos = str(input("¿Desea calcular la suma de pares o impares? (pares/impares):" ))
        if que_calculamos != "pares" and que_calculamos != "impares":
            error = 2
            raise ValueError
        # Proceso
        suma_especiales = numeros_especiales(inicio, final, que_calculamos)
        # Salida
        print(f"La suma de los numeros {que_calculamos} que no son múltiplos de 3 en el rango "
        f"de {inicio} a {final} es: {suma_especiales}")
    except ValueError:
        # Salida
        if error == 1:
            ""
        elif error == 2:
            print("Ingrese adecuadamente que calcular")

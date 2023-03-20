
# Conocer si un número ingresado es primo
# aplicando recursividad
# Se agrega tipado estatico en la función

def nroPrimo(num: int, d:int):
    if num//2 < d:
        return True
    elif (num % 2)== 0:
        return False
    elif (num % 3)== 0:
        return False
    elif (num % 5)== 0:
        return False
    elif (num % 7)== 0:
        return False
    else:
        return nroPrimo(num, d+1)

# Programa principal

nro = int(input('Ingrese un número '))
if nroPrimo(nro,2):
    print('Número ',nro,' es primo')
else:
    print('Número ',nro,' no es primo')

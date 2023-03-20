def decorador(func):
    def envoltura():
        print('Esto se añade a mi función original')
        func()
    return envoltura

""" La siguiente función con la posterior asignación a la variable saludo es equivalente 
    al decorador que está en la función @decorador

def saludo():
    print('¡Hola!')
saludo = decorador(saludo)

"""

@decorador
def saludo():
    print('¡Hola!')

Saludo()



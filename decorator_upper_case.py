def mayusculas(funcion):
    def envoltura(texto):
        return funcion(texto).upper()
    return envoltura

@mayusculas
def mensaje(nombre):
    return f'{nombre}, recibiste un mensaje'
print(mensaje('Cesar'))


def mayusculas(funcion):
    def envoltura(texto: str):
        return funcion(texto).upper()
    return envoltura

def mensaje(nombre):
   return f'{nombre}, recibiste un mensaje'
mensaje = mayusculas(mensaje)
print(mensaje('Cesar'))

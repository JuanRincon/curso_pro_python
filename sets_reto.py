# [1, 1, 2, 2, 4] -> [1, 2, 4]

# Crea un programa que elimine los elementos repetidos de una lista, pero en lugar de utilizar un 
# ciclo for utiliza sets.

""" Aquí tenemos una función que hace lo mismo que un set pero con un ciclo for, sin el uso directo
    de lo que hace set

    def remove_duplicates(some_list):
    without_duplicates = []
    for element in some_list:
        if element not in without_duplicates:
            without_duplicates.append(element)
    return without_duplicates

def run():
    random_list = [1, 1, 2, 2, 4]
    print(remove_duplicates(random_list))
  

if __name__ == '__main__':
    run()
"""
# En esta parte se ejecuta como tal el reto con set

def remove_duplicates(some_list):
    without_duplicates = set(some_list)
    return without_duplicates


def run():
    random_list = [1, 1, 2, 2, 4]
    print(remove_duplicates(random_list))
  

if __name__ == '__main__':
    run()

# Es importante notar la simplicidad de hacer este ejercicio con set

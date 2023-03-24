""" Este programa lo que hace es repetir una cadena de
caracteres, la cantidad de veces que le especifiquemos
"""
# Hola 3 -> HolaHolaHola
# Facundo 2 -> FacundoFacundo
# Platzi 4 -> PlatziPlatziPlatziPlatzi

def make_repeater_of(n):
    def repeater(string):
        assert type(string) == str, "Solo puede utilizar cadenas"
        return string * n
    return repeater

def run():
    repeat_5 = make_repeater_of(5)
    repeat_10 = make_repeater_of(10)
    print(repeat_5("Hola"))
    print(repeat_10("Platzi"))
    
if __name__ == '__main__':
    run()

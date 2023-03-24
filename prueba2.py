import time

def conteo():
    light = 1
    i = 0   
    def color():
        while i < 10:
            if light == 1:
                i += 1
                print('Verde')
                time.sleep(1)
                light = 2
            elif light == 2:
                i += 1
                print('Amarillo')
                time.sleep(1)
                light = 3
            else:
                i += 1
                print('Rojo')
                time.sleep(1)
                light = 1
    return color()

color_light = conteo()
color_light()

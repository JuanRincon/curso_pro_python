
import time

def conteo(element):
    def color(light):
        while element < 10:
            if light == 1:
                element += 1
                print("verde")
                time.sleep(5)
                light = 2
            elif light == 2:
                element += 1
                print("amarillo")
                time.sleep(5)
                light = 3
            else:
                element += 1
                print("rojo")
                time.sleep(5)
                light = 1
    color(light)


light_color = conteo(0)
print(light_color(1))

import time

def conteo(funtion):
    light = 1
    def color():
        i = 0
        while i < 10:
            if light == 1:
                i += 1
                time.sleep(5)
                light = 2
            elif light == 2:
                i += 1
                time.sleep(5)
                light = 3
            else:
                i += 1
                time.sleep(5)
                light = 1
        funtion()
    return color


@conteo
def semaforo():
    # if light_red:
     #   print('stop')
    # elif light_yellow:
     #   print('wait')
    # else:
     #   print('continue or start')
    print(light)


def run():
    semaforo()


if __name__ == '__main__':
    run()

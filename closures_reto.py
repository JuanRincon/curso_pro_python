def make_division_by(n):
    """This closure returns a funtion that returns the division
        of an x number by n
    """
    def division(x):
        div = x/n
        return div

    return division


def run():
    cociente_5 = make_division_by(5)
    print(cociente_5(100))

    cociente_3 = make_division_by(3)
    print(cociente_3(18))
    
    cociente_18 = make_division_by(18)
    print(cociente_18(54))


if __name__ == '__main__':
    run()

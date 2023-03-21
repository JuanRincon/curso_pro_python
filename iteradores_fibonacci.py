import time

class FiboIter():

    def __init__(self, max=377):
        self.max = max


    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        self.aux = 0
        return self


    def __next__(self):
        if not self.max or self.aux < self.max:
            if self.counter == 0:
                self.counter +=1
                return self.n1
            elif self.counter == 1:
                self.counter +=1
                return self.n2
            else:
                self.aux = self.n1 + self.n2
                #self.n1 = self.n2       """ Esta línea y la de abajo son reemplazadas por la 
                #self.n2 = self.aux          función suapping que encontramos en la siguiente línea son comentar """
                self.n1, self.n2 = self.n2, self.aux
                self.counter += 1
                return self.aux
        else:
            raise StopIteration
        

if __name__ == '__main__':
    fibonacci = FiboIter()
    for element in fibonacci:
        print(element)
        time.sleep(0.2)

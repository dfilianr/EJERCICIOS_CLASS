class pila:
    def __init__(self,tamanio=5):
        self.lista = []
        self.size = tamanio
        self.top = 0
    
    def push (self,dato):
        if self.top < self.size:
            self.lista = self.lista + [dato]
            self.top += 1
        else:
            print("La lista esta llena")

    def pop(self):
        if self.empty():
            return None
        else:
            top = self.lista[-1]
            self.lista = self.lista[:self.top]
            self.top -= 1
            return top

    def show(self):
        for top in range(self.top-1,-1,-1):
            print("[{}]".format(self.lista[top]))

    def longitud(self):
        return self.top


    def empty(self):
        if self.top == 0:
            return True
        else:
            return False

pila1 = pila(5)
pila1.push(8)
pila1.push(10)
pila1.push(12)
pila1.push(4)
dato = pila1.pop()
pila1.show()
pila1.longitud()
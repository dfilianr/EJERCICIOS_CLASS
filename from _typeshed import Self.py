
class Busqueda:
    def __init__(self,listas) :
        self.__lista= listas
    @property
    def lista(self) :
        return self.__lista   

    def busquedalineal(self,buscado):
        lon= len(self.lista)
        posicion=0
        encontr= False
        while posicion < lon and encontr==False:
            if self.lista[posicion]["nombre"] == buscado : encontr=True
            else: posicion+=1  
        if encontr:return posicion
        else: return -1    
    def ordenar(self):
        pass
    def busquedabinaria(self, buscando):
        pass
nota= [{"nombre","erikc","n1",40,"n2",50},{"nombre","patrick","n1",25,"n2",70},
        {"nombre","andres","n1",35,"n2",30}, {"nombre","dario","n1",50,"n2",50}
       ]

      

from abc import ABC, abstractmethod
class Obra(ABC):
    def __init__(self, titulo, artista, ano):
        self.__titulo=titulo
        self.__artista=artista
        self.__ano=ano
    @abstractmethod
    def mostrar(self):
        pass
    def getTitulo(self):
        return self.__titulo
    def getArtista(self):
        return self.__artista
    def getAno(self):
        return self.__ano
    def setTitulo(self,titulo):
        self.__titulo=titulo
    def setArtista(self,artista):
        self.__artista=artista
    def setAno(self,ano):
        self.__ano=ano
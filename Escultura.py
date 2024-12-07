from Obra import Obra
class Escultura(Obra):
    def __init__(self, titulo, artista, ano, modelo):
        super().__init__(titulo, artista, ano)
        self.__modelo=modelo
    def setModelo(self,modelo):
        self.__modelo = modelo
    def getModelo(self):
        return self.__modelo
    def mostrar(self):
        return (f"Escultura: {self.getTitulo()}, Artista: {self.getArtista()}, Ano {self.getAno()}, e Modelo {self.getModelo()} foi criado")
from Obra import Obra
class Quadro(Obra):
    def __init__(self, titulo, artista, ano, cor):
        super().__init__(titulo, artista, ano)
        self.__cor=cor
    def setCor(self,cor):
        self.__cor = cor
    def getCor(self):
        return self.__cor
    def mostrar(self):
        return (f"Quadro: {self.getTitulo()}, Artista: {self.getArtista()}, Ano {self.getAno()}, e Cor {self.getCor()} foi criado")
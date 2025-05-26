from Entidades.Categoria import Categoria
from Entidades.MembroAcademia import MembroAcademia

class Indicacao:
    def __init__(self, indicado, categoria: Categoria, membroAcademia: MembroAcademia):
        self.__categoria = categoria
        self.__indicado = indicado
        self.__membroAcademia = membroAcademia

    @property
    def categoria(self) -> Categoria:
        return self.__categoria
    
    @property
    def indicado(self):
        return self.__indicado
    
    @property
    def membro(self):
        return self.__membroAcademia
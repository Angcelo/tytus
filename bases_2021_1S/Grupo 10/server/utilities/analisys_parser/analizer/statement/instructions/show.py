from utilities.analisys_parser.analizer.reports import Nodo
from utilities.storage import avlMode
from utilities.analisys_parser.analizer.abstract.instruction import Instruction


class showDataBases(Instruction):
    def __init__(self, like, row, column):
        Instruction.__init__(self, row, column)
        if like != None:
            self.like = like[1 : len(like) - 1]
        else:
            self.like = None

    def execute(self, environment):
        lista = []
        if self.like != None:
            for l in avlMode.showDatabases():
                if self.like in l:
                    lista.append(l)
        else:
            lista = avlMode.showDatabases()
        if len(lista) == 0:
            return "No hay bases de datos"
        return lista

    def dot(self):
        new = Nodo.Nodo("SHOW_DATABASES")
        if self.like != None:
            l = Nodo.Nodo("LIKE")
            ls = Nodo.Nodo(self.like)
            new.addNode(l)
            l.addNode(ls)

        return new

from Models import *
from DAO import *


class CategoriaController:
    def Salvar(self, novaCategoria):
        with open('Categoria.txt', 'r') as arq:
            existe = False
            for i in arq.readlines():
                if i.lower().replace('\n', '') == novaCategoria.lower():
                    existe = True
            if existe == False:
                if len(str(novaCategoria).replace(' ', '')) < 4 or len(str(novaCategoria)) > 10:
                    print('Categoria inválida!')
                else:
                    CategoriaDAO.Salvar(novaCategoria)
            else:
                print('Categoria já existe!')


a = CategoriaController()
a.Salvar('Cereais')

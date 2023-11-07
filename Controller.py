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
                    print('Categoria ', novaCategoria, ' cadastrada com sucesso!')
            else:
                print('Categoria já existe!')

    def Remover(self, removerCategoria):
        with open('Categoria.txt', 'r') as arq:
            existe = False
            categorias = arq.readlines()
            for i in categorias:
                if i.lower().replace('\n', '') == removerCategoria.lower():
                    existe = True
            if existe:
                with open('Categoria.txt', 'w') as arq1:
                    for i in categorias:
                        if i.lower().replace('\n', '') != removerCategoria.lower():
                            CategoriaDAO.Salvar(i.replace('\n', ''))
                print('Categoria ', removerCategoria, ' removida com sucesso!')
            else:
                print('Categoria não encontrada!')


class ProdutosController:
    def Salvar(self, novoproduto: Produtos):
        with open('Produtos.txt', 'r') as arq:
            existe = False
            produtos = arq.readlines()
            for i in produtos:
                if i.lower().split('|')[0] == str(novoproduto.nome).lower():
                    existe = True
            if existe:
                return 'Produto já existente!'
            else:
                ProdutosDAO().Salvar(Produtos(novoproduto.nome, novoproduto.categoria, novoproduto.preco))
                return print('Produto', novoproduto.nome, ' salvo com sucesso!')

    def Remover(self, removerproduto):
        with open('Produtos.txt', 'r') as arq:
            produtos = arq.readlines()
            existe = False
            for i in produtos:
                if i.lower().split('|')[0] == str(removerproduto).lower():
                    existe = True
            if not existe:
                print(removerproduto, ' não foi encontrado!')
            else:
                with open('Produtos.txt', 'w') as arq:
                    for i in produtos:
                        if i.lower().split('|')[0] != removerproduto.lower():
                            ProdutosDAO().Salvar(Produtos(i.split('|')[0], i.split('|')[1], i.split('|')[2].replace('\n', '')))
                print(removerproduto, ' removido com sucesso!')


a = ProdutosController()
a.Remover('Banana')

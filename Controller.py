from sre_compile import isstring

from Models import *
from DAO import *


class CategoriaController:
    def AdicionarCategoria(self, novaCategoria):
        for i in novaCategoria:
            if i.isnumeric() or len(str(novaCategoria)) > 10 or len(str(novaCategoria)) < 4:
                print("Categoria inválida!")
                break
        for i in CategoriaDAO.Ler():
            if str(i).lower().replace('\n', '') == str(novaCategoria).lower():
                print ('Essa categoria já está cadastrada')


    def RemoverCategoria(self, categoriaRemover):
        categorias = []
        for i in CategoriaDAO.Ler():
            categorias.append(i.replace('\n', '').lower())
        if str(categoriaRemover).lower() not in categorias:
            print('Categoria não encontrada')
        else:
            with open('Categorias.txt', 'w') as arq:
                for i in categorias:
                    if i == categoriaRemover.lower():
                        pass
                    else:
                        arq.writelines(i + '\n')

    def AlterarCategoria(self, categoriaAntiga, categoriaNova):
        categorias = []
        existe = False
        for i in CategoriaDAO.Ler():
            categorias.append(i.replace('\n', ''))
            if i.replace('\n', '').lower() == str(categoriaAntiga).lower():
                existe = True
        if not existe:
            print('Categoria {} não encontrada.'.format(categoriaAntiga))
        else:
            with open('Categorias.txt', 'w') as arq:
                for i in categorias:
                    if i.lower() == categoriaAntiga.lower():
                        pass
                    else:
                        arq.writelines(i + '\n')
                arq.writelines(categoriaNova + '\n')
            print('Categoria alterada.')


class ProdutosController:
    def AdicionarProduto(self, produtos: Produtos):
        existe = False
        for i in ProdutosDAO.Ler():
            if i.split('|')[0].lower() == str(produtos.nome).lower():
                existe = True
                break
        if existe:
            print('Produto {} já existe.'.format(produtos.nome))
        else:
            ProdutosDAO.Salvar(Produtos(produtos.nome, produtos.categoria, str(produtos.preco)))
            print('Produto {} salvo com sucesso!'.format(produtos.nome))


    def ExcluirProduto(self, produtoExcluir):
        existe = False
        produtos = ProdutosDAO.Ler()
        for i in produtos:
            if i.split('|')[0].lower() == str(produtoExcluir).lower():
                existe = True
        if existe:
            with open('Produtos.txt', 'w'):
                for i in produtos:
                    if i.split('|')[0].lower() != str(produtoExcluir).lower():
                        ProdutosDAO.Salvar(Produtos(i.split('|')[0], i.split('|')[1], i.split('|')[2].replace('\n', '')))
        else:
            print('Produto não encontrado')


    def AlterarProduto(self, produtoAnterior, produtoNovo:Produtos):
        produtos = ProdutosDAO.Ler()
        existeAnterior = False
        existeNovo = False
        for i in produtos:
            if i.split('|')[0].lower() == str(produtoAnterior).lower():
                existeAnterior = True
            if i.split('|')[0].lower() == str(produtoNovo.nome).lower():
                produtoNovo = True
        if not existeAnterior:
            print('Produto não encontrado')
        elif existeNovo:
            print('Produto {} já tem cadastrado.'.format(produtoNovo))



a = ProdutosController()
a.AlterarProduto('cenouras', Produtos('Abacate', 'Frutas', 4.99))
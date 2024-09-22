from Models import *


class CategoriaDAO:
    @classmethod
    def Salvar(cls, categoria):
        with open('Categorias.txt', 'a') as arq:
            arq.writelines(categoria + '\n')

    @classmethod
    def Ler(cls):
        with open('Categorias.txt', 'r') as arq:
            return arq.readlines()


class ProdutosDAO:
    @classmethod
    def Salvar(cls, produto:Produtos):
        with open('Produtos.txt', 'a') as arq:
            arq.writelines(produto.nome + '|' + produto.categoria + '|' + produto.preco + '\n')

    @classmethod
    def Ler(cls):
        with open('Produtos.txt', 'r') as arq:
            return arq.readlines()


class EstoqueDAO:
    @classmethod
    def Salvar(cls, estoque:Estoque):
        with open('Estoque.txt', 'a') as arq:
            arq.writelines(estoque.produto.nome + '|' + estoque.produto.categoria + '|' +
                           estoque.produto.preco + '|' + estoque.quantidade + '\n')

    @classmethod
    def Ler(cls):
        with open('Estoque.txt', 'r') as arq:
            return arq.readlines()


class VendasDAO:
    @classmethod
    def Salvar(cls, venda:Vendas):
        with open('Vendas.txt', 'a') as arq:
            arq.writelines(venda.itemVendido.categoria + '|' + venda.itemVendido.nome + '|' +
                           venda.itemVendido.preco + '|' + venda.vendedor + '|' +
                           venda.comprador + '|' + venda.quantidadeVendida + '\n')

    @classmethod
    def Ler(cls):
        with open('Vendas.txt', 'r') as arq:
            return arq.readlines()




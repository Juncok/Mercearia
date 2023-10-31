from Models import *


class CategoriaDAO:
    @classmethod
    def Salvar(cls, categoria):
        with open('Categoria.txt', 'a') as arq:
            arq.writelines(categoria + '\n')

    @classmethod
    def Ler(cls):
        with open('Categoria.txt', 'r') as arq:
            for i in arq.readlines():
                print(i.replace('\n', ''))


class ProdutosDAO:
    @classmethod
    def Salvar(cls, produtos: Produtos):
        with open('Produtos.txt', 'a') as arq:
            arq.writelines(produtos.nome + '|' + produtos.categoria + '|' + str(produtos.preco) + '\n')

    @classmethod
    def Ler(cls):
        with open('Produtos.txt', 'r') as arq:
            cls.produtos = arq.readlines()
            prod = []
            for i in cls.produtos:
                prod.append(Produtos(i.split('|')[0], i.split('|')[1], i.split('|')[2]))
            return prod

class EstoqueDAO:
    @classmethod
    def Salvar(cls, estoque: Estoque):
        with open('Estoque.txt', 'a') as arq:
            arq.writelines(estoque.produto.nome + '|' + estoque.produto.categoria + '|' +
                           str(estoque.produto.preco) + '|' + str(estoque.quantidade) + '\n')

    @classmethod
    def Ler(cls):
        with open('Estoque.txt', 'r') as arq:
            cls.estoque = arq.readlines()
            estoque = []
            for i in cls.estoque:
                estoque.append(Estoque(Produtos(i.split('|')[0], i.split('|')[1], i.split('|')[2])
                                       , i.split('|')[3]))
            return estoque


class VendaDAO:
    @classmethod
    def Salvar(cls, venda: Venda):
        with open('Vendas.txt', 'a') as arq:
            arq.writelines(venda.itemVendido.nome + '|' + venda.itemVendido.categoria + '|' + str(venda.itemVendido.preco) +
                           '|' + str(venda.quantidadeVendida) + '|' + venda.vendedor + '|' + venda.comprador + '\n')


    @classmethod
    def Ler(cls):
        with open('Vendas.txt', 'r') as arq:
            cls.venda = arq.readlines()
            vendas = []
            for i in cls.venda:
                vendas.append(Venda(Produtos(i.split('|')[0], i.split('|')[1], i.split('|')[2]),
                                    i.split('|')[3], i.split('|')[4], i.split('|')[5]))
            return vendas


a = VendaDAO()
print(a.Ler()[0].comprador)
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

    def Alterar(self, categoriaantiga, categorianova):
        with open('Categoria.txt', 'r') as arq:
            categorias = arq.readlines()
            existeAntiga = False
            existeNova = False
            for i in categorias:
                if i.lower().replace('\n', '') == str(categoriaantiga).lower():
                    existeAntiga = True
                if i.lower().replace('\n', '') == str(categorianova).lower():
                    existeNova = True
            if not existeAntiga:
                print('Categoria ', categoriaantiga, ' não encontrada!')
            elif existeNova:
                print('Categoria ', categorianova, ' já existe!')
            else:
                with open('Categoria.txt', 'w') as arq:
                    for i in categorias:
                        if i.lower().replace('\n', '') != categoriaantiga.lower():
                            CategoriaDAO().Salvar(i.replace('\n', ''))
                    CategoriaDAO().Salvar(categorianova)
                    print('Categora ', categoriaantiga, ', alterada para ', categorianova,' com sucesso!')


    def Ler(self):
        with open('Categoria.txt', 'r') as arq:
            for i in arq.readlines():
                print(i.replace('\n', ''))


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


class EstoqueController:
    def Salvar(self, produto:Produtos, quantidade):
        e = []
        c = []
        for i in EstoqueDAO.Ler():
            e.append(str(i.produto.nome).lower())
        for i in CategoriaDAO.Ler():
            c.append(i.lower())
        if str(produto.nome).lower() in e:
            print('O produto', produto.nome, 'já consta no estoque!')
        elif str(produto.categoria).lower() not in c:
            print('A categoria', produto.categoria, 'não existe!')
        else:
            EstoqueDAO.Salvar(Estoque(Produtos(produto.nome, produto.categoria, produto.preco), quantidade))

    def Ler(self):
        print('-'*8, 'ESTOQUE', '-'*8)
        for i in EstoqueDAO.Ler():
            print('Produto: ', i.produto.nome, ' - Categoria: ', i.produto.categoria, ' - Quantidade: ', i.quantidade.replace('\n', ''))

    def Remover(self, estoqueRemover):
        existe = False
        estoque = EstoqueDAO.Ler()
        for i in estoque:
            if i.produto.nome.lower() == estoqueRemover.lower():
                existe = True
        if not existe:
            print(estoqueRemover, 'não foi encontrado!')
        else:
            with open('Estoque.txt', 'w') as arq:
                for i in estoque:
                    if i.produto.nome.lower() != estoqueRemover.lower():
                        EstoqueDAO.Salvar(Estoque(Produtos(i.produto.nome, i.produto.categoria, i.produto.preco),
                                                  i.quantidade.replace('\n', '')))
            print(estoqueRemover, 'removido com sucesso!')


class VendaController:
    def Salvar(self, venda: Venda):
        estoque = EstoqueDAO.Ler()
        existe = False
        quantidade = 0
        for i in estoque:
            if i.produto.nome.lower() == venda.itemVendido.nome.lower():
                existe = True
                quantidade = int(i.quantidade)
        if not existe:
            print(venda.itemVendido.nome, 'não foi encontrado na estoque!')
        elif quantidade < venda.quantidadeVendida:
            print('Quantidade insuficiente do produto!')
        else:
            VendaDAO.Salvar(Venda(Produtos(venda.itemVendido.nome, venda.itemVendido.categoria, venda.itemVendido.preco),
                                  venda.quantidadeVendida, venda.vendedor, venda.comprador))
            print(venda.itemVendido.nome, 'cadastrado com sucesso!')

    def Relatorio(self):
        vendas = []
        for i in VendaDAO.Ler():
            produto = i.itemVendido.nome
            quantidade = int(i.quantidadeVendida)
            iguais = list(filter(lambda x: produto == x['produto'], vendas))
            if len(iguais) == 0:
                vendas.append({'produto': produto, 'quantidade': quantidade})
            else:
                vendas = list(map(lambda x: {'produto': produto, 'quantidade': quantidade + x['quantidade']}
                                             if x['produto'] == produto else x, vendas))

        ordenado = sorted(vendas, key=lambda k: k['quantidade'])
        print('QUANTIDADE', 12*'=', 'PRODUTO\n', 28*'-')
        for i in ordenado:
            print(i['quantidade'], 20*'=', i['produto'])
        return ordenado


a = VendaController()
print(a.Relatorio())

from DAO import *



class VendaController:

    def relatoriocontroller(self):
        vendas = []
        for i in VendaDAO.Ler():
            produto = i.itemVendido.nome
            quantidade = int(i.quantidadeVendida)
            multiplos = list(filter(lambda x: x['produto'] == produto, vendas))
            if len(multiplos) == 0:
                vendas.append({'produto': produto, 'quantidade': quantidade})
            else:
                vendas = list(map(lambda x: {'produto': produto, 'quantidade': x['quantidade'] + quantidade}
                if (x['produto'] == produto) else x, vendas))

        return vendas


a = VendaController()
print(a.relatoriocontroller())

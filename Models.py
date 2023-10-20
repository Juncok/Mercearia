class Categoria:
    def __int__(self, categoria):
        self.categoria = categoria

class Produtos:
    def __int__(self, nome, categoria:Categoria, preco):
        self.nome = nome
        self.categoria = categoria
        self.preco = preco

class Estoque:
    def __init__(self, produto:Produtos, quantidade):
        self.produto = produto
        self.quantidade = quantidade


class Venda:
    def __int__(self, itemVendido:Produtos, quantidadeVendida, vendedor, comprador):
        self.itemVendido = itemVendido
        self.quantidadeVendida = quantidadeVendida
        self.vendedor = vendedor
        self.comprador = comprador


class Fornecedor:
    def __int__(self, nome, cnpj, telefone, categoria:Categoria):
        self.nome = nome
        self.cnpj = cnpj
        self.telefone = telefone
        self.categoria = categoria


class Pessoa:
    def __init__(self, nome, telefone, cpf, email, endereco):
        self.nome = nome
        self.telefone = telefone
        self.cpf = cpf
        self.email = email
        self.endereco = endereco


class Funcionario(Pessoa):
    def __int__(self, clt, nome, telefone, cpf, email, endereco):
        self.clt = clt
        super(Funcionario, self).__init__(nome, telefone, cpf, email, endereco)
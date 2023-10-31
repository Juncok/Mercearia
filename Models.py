class Categoria:
    def __init__(self, categoria):
        self.categoria = categoria


class Produtos:
    def __init__(self, nome, categoria: Categoria, preco):
        self.nome = nome
        self.categoria = categoria
        self.preco = preco


class Estoque:
    def __init__(self, produto: Produtos, quantidade):
        self.produto = produto
        self.quantidade = quantidade


class Venda:
    def __init__(self, itemVendido: Produtos, quantidadeVendida, vendedor, comprador):
        self.itemVendido = itemVendido
        self.quantidadeVendida = quantidadeVendida
        self.vendedor = vendedor
        self.comprador = comprador


class Fornecedor:
    def __init__(self, nome, cnpj, telefone, email, endereco):
        self.nome = nome
        self.cnpj = cnpj
        self.telefone = telefone
        self.email = email
        self.endereco = endereco


class Pessoa:
    def __init__(self, nome, cpf, telefone, email, endereco):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.email = email
        self.endereco = endereco


class Vendedor(Pessoa):
    def __init__(self, cnpj, nome, cpf, telefone, email, endereco):
        self.cnpj = cnpj
        super(Vendedor, self).__init__(nome, cpf, telefone, email, endereco)

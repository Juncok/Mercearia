class Categorias:
    def __init__(self, categoria):
        self.categoria = categoria


class Produtos:
    def __init__(self, nome, categoria, preco):
        self.nome = nome
        self.categoria = categoria
        self.preco = preco


class Estoque:
    def __init__(self, produto: Produtos, quantidade):
        self.produto = produto
        self.quantidade = quantidade


class Fornecedor:
    def __init__(self, categoria:Categorias, cnpj, nome, telefone, email):
        self.categoria = categoria
        self.cnpj = cnpj
        self.nome = nome
        self.telefone = telefone
        self.email = email


class Vendas:
    def __init__(self, itemVendido:Produtos, vendedor, comprador, quantidadeVendida):
        self.itemVendido = itemVendido
        self.vendedor = vendedor
        self.comprador = comprador
        self.quantidadeVendida = quantidadeVendida


class Pessoa:
    def __init__(self, cpf, nome, telefone, email, endereco):
        self.cpf = cpf
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco


class Vendedor(Pessoa):
    def __init__(self, clt, cpf, nome, telefone, email, endereco):
        self.clt = clt
        super(Vendedor).__init__(cpf, nome, telefone, email, endereco)
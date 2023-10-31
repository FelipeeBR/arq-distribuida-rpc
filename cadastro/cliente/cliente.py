import xmlrpc.client
from datetime import datetime

class ClienteRPC(object):
    '''
        Cliente leve (thin client) usando RPC
    '''

    def __init__(self):
        self.server = xmlrpc.client.ServerProxy("http://localhost:7080")

    def addCliente(self, nome, dtNascimento, cpf, logradouro, num,
        bairro, cidade, estado):
        self.server.addCliente(nome, dtNascimento, cpf, logradouro,
            num, bairro, cidade, estado)

    def getCliente(self, idCliente):
        c = self.server.getCliente(idCliente)
        return c

    def getClientes(self):
        c = self.server.getClientes()
        return c 

    def getClientesPorNome(self, nome):
        c = self.server.getClientesPorNome(nome)
        return c 

    def delCliente(self, idCliente):
        c = self.server.delCliente(idCliente)


    
    def addVenda(self, dtVenda, valor, produto, quantidade, cliente_id):
        self.server.addVenda(dtVenda, valor, produto, quantidade, cliente_id)
    
    def getVenda(self, idVenda):
        v = self.server.getVenda(idVenda)
        return v
        
if __name__ == "__main__":
     
    print("\n---- Instanciando a aplicação ----")
    app = ClienteRPC()

    #print("\n---- Adicionando um cliente ----")
    #app.addCliente("Felipe", datetime(1998, 3, 20), '11122233344',
    #                "rua", "0", "bairro", "cidade", "MG")
    

    print("\n--- Adicionando uma Venda ----")
    app.addVenda(datetime(2011, 8, 22), 499, 'Pendrive', 5, 1)
    
    print("\n---- Pesquisando e imprimindo os dados do cliente ----")
    c = app.getCliente(1)
    print(c)

    print("\n---- Pesquisando Venda ----")
    v = app.getVenda(1)
    print(v)

    cs = app.getClientesPorNome("ni")
    print(cs)

    # print("\n---- Deletando os dados do cliente ----")
    #app.delCliente(1)
    #cs = app.getClientes()
    #print(cs)

from twisted.web import xmlrpc
import db
from cadastro import CadastroCTRL

class ServerRPC(xmlrpc.XMLRPC):
    '''
        Servidor RPC para a camada de negócio
    '''

    def __init__(self, allowNone):
        super().__init__(allowNone)
        db.startDatabase()
        self.fachada = CadastroCTRL()

    def xmlrpc_addCliente(self, nome, dtNascimento, cpf, logradouro, num, 
        bairro, cidade, estado):
        new_id = self.fachada.addCliente(nome, 
                                     dtNascimento, 
                                     cpf, 
                                     logradouro, 
                                     num,
                                     bairro, 
                                     cidade, 
                                     estado)
        return new_id

    def xmlrpc_getCliente(self, idCliente):
        c = self.fachada.getCliente(idCliente)
        return c
    
    def xmlrpc_getClientes(self):
        c = self.fachada.getClientes()
        return c

    def xmlrpc_getClientesPorNome(self, nome):
        c = self.fachada.getClientesPorNome(nome)
        return c

    def xmlrpc_delCliente(self, idCliente):
        self.fachada.delCliente(idCliente)

    
    #Venda
    def xmlrpc_addVenda(self, dtVenda, valor, produto, quantidade, cliente_id):
        new_id = self.fachada.addVenda(dtVenda, 
                                     valor, 
                                     produto, 
                                     quantidade, cliente_id)
        return new_id
    
    def xmlrpc_getVenda(self, idVenda):
        v = self.fachada.getVenda(idVenda)
        return v

#TODO add exception handler and log
#TODO add security layer for clients apps authentication
#TODO add ciphering data
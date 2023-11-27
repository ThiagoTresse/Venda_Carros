from datetime import date
from model.clientes import Cliente
from model.veiculos import Veiculo

class VendaVeiculo:
    def __init__(self, 
                 idVenda:int=None,
                 valorVenda:float=None,
                 dataVenda:int=None,
                 idVendedor:int=None,
                 Cliente:str=None,
                 Veiculo:str=None
                 ):
        self.set_idVenda(idVenda)
        self.set_valorVenda(valorVenda)
        self.set_dataVenda(dataVenda)
        self.set_idVendedor(idVendedor)
        self.set_cliente(Cliente)
        self.set_veiculos(Veiculo)
#Getters
    def get_idVenda(self) -> int:
        return self.idVenda

    def get_valorVenda(self) -> float:
        return self.valorVenda
    
    def get_dataVenda(self) -> int:
        return self.datavenda

    def get_idVendedor(self) -> int:
        return self.idVendedor

    def get_cliente(self) -> Cliente:
        return self.cliente

    def get_veiculos(self) -> Veiculo:
        return self.veiculos

#Setters
    def set_idVenda(self, idVenda: int):
        self.idVenda = idVenda

    def set_valorVenda(self, valorVenda: float):
        self.valorVenda = valorVenda

    def set_dataVenda(self, dataVenda: int):
        self.datavenda = dataVenda

    def set_idVendedor(self, idVendedor: int):
        self.idVendedor = idVendedor

    def set_cliente(self, cliente: Cliente):
        self.cliente = cliente

    def set_veiculos(self, veiculos: Veiculo):
        self.veiculos = veiculos

#ToString
    def to_string(self) -> str:
        return (f"idVenda: {self.get_idVenda()} | valorVenda: {self.get_valorVenda()} | dataVenda: {self.get_dataVenda()} | idVendedor: {self.get_idVendedor()} | cpfCliente: {self.get_cliente().get_cpfCliente()} | Veiculo: {self.get_veiculos().get_idCarro()}")

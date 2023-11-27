from datetime import date
from model.clientes import Cliente
from model.veiculos import Veiculo

class VendaVeiculo:
    def __init__(self, 
                 idVenda:int=None,
                 valorVenda:float=None,
                 dataVenda:int=None,
                 idVendedor:int=None,
                 cliente:Cliente=None,
                 veiculo:Veiculo=None
                 ):
        self.set_idVenda(idVenda)
        self.set_valorVenda(valorVenda)
        self.set_dataVenda(dataVenda)
        self.set_idVendedor(idVendedor)
        self.set_cliente(cliente)
        self.set_veiculo(veiculo)
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

    def get_veiculo(self) -> Veiculo:
        return self.veiculo

#Setters
    def set_idVenda(self, idVenda: int):
        self.idVenda = idVenda

    def set_valorVenda(self, valorVenda: float):
        self.valorVenda = valorVenda

    def set_dataVenda(self, dataVenda: int):
        self.datavenda = dataVenda

    def set_idVendedor(self, idVendedor: int):
        self.idVendedor = idVendedor

    def set_cliente(self, cliente:Cliente):
        self.cliente = cliente

    def set_veiculo(self, veiculo: Veiculo):
        self.veiculo = veiculo

#ToString
    def to_string(self) -> str:
        return (f"idVenda: {self.get_idVenda()} | "
                f"valorVenda: {self.get_valorVenda()} | "
                f"dataVenda: {self.get_dataVenda()} | " 
                f"idVendedor: {self.get_idVendedor()} | "
                f"cliente: {self.get_cliente().get_cpfCliente()} | "
                f"veiculo: {self.get_veiculo().get_idCarro()}"
        )
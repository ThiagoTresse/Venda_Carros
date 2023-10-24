from pydoc import cli
from model.clientes import Cliente
from controller.controller_cliente import Controller_Cliente
from model.veiculos import Veiculo
from controller.controller_veiculo import Controller_Veiculo
from model.Venda import VendaVeiculo
from conexion.oracle_queries import OracleQueries
from datetime import date
import random

class Controller_Venda:
    def __init__(self):
        self.ctrl_cliente = Controller_Cliente()
        self.ctrl_veiculo = Controller_Veiculo()
        
    def inserir_venda(self) -> VendaVeiculo:
        ''' Ref.: https://cx-oracle.readthedocs.io/en/latest/user_guide/plsql_execution.html#anonymous-pl-sql-blocks'''
        
        # Cria uma nova conexão com o banco
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        # Lista os clientes existentes para inserir no pedido
        self.listar_clientes(oracle, need_connect=True)
        cpfCliente = int(input("Digite o número do CPF do Cliente para adicionar a Venda: "))
        Cliente = self.valida_cliente(oracle, cpfCliente)
        if Cliente == None:
            return None

        # Lista os Veiculos existentes para inserir no pedido
        self.listar_veiculos(oracle, need_connect=True)
        idCarro = int(input("Digite o número do id do Veiculo para adicionar a Venda: "))
        Veiculo = self.valida_veiculo(oracle, idCarro)
        if Veiculo == None:
            return None

        data_hoje = date.today()
        print("Data de hoje: " (data_hoje))

        if self.verifica_prevenda(oracle, cpfCliente, idCarro):
            #Sistema gera a data da venda com a data de hoje
            dataVenda = data_hoje
            #Solicita ao usuario o valor da venda
            valorVenda = input("Informe o valor da venda: ")
            #Solicita ao usuario o id do vendedor
            idVendedor = input("Informe o id do vendedor: ")
            #Sistema gera um id de venda aleatorio
            idVenda = random.randint(1000,9999)
            print = ("o ID da Venda é: " (idVenda))
        # Recupera o cursor para executar um bloco PL/SQL anônimo
        cursor = oracle.connect()
        # Cria a variável de saída com o tipo especificado
        output_value = cursor.var(int)

        # Cria um dicionário para mapear as variáveis de entrada e saída         
        data = dict(VendaVeiculo=output_value, dataVenda=data_hoje, idVenda=VendaVeiculo.get_idVenda(), valorVenda=VendaVeiculo.get_valorVenda(),
                    idVendedor=VendaVeiculo.get_idVendedor(),  cpfCliente=VendaVeiculo.get_cpfCliente(), idCarro=VendaVeiculo.get_idCarro()) 
        # Executa o bloco PL/SQL anônimo para inserção da nova venda e recuperação da chave primária criada pela sequence
        cursor.execute("""
        begin
            :idVenda := idVenda_SEQ.NEXTVAL;    
            insert into VendaVeiculo values(:idVenda, :valorVenda, :dataVenda, :idVendedor, :cpfCliente, :idCarro);
        end;
        """, data) 
        # Recupera o código da nova venda
        idVenda = output_value.getvalue()
        # Persiste (confirma) as alterações
        oracle.conn.commit()
        # Recupera os dados do novo pedido criado transformando em um DataFrame
        df_venda = oracle.sqlToDataFrame(f"select idVenda, valorVenda, dataVenda, idVendedor, cpfCliente, idCarro from vendaVeiculos where idVenda = {idVenda}")
        # Cria um novo objeto venda
        nova_venda = VendaVeiculo(df_venda.idVenda.values[0], df_venda.valorVenda.values[0], df_venda.dataVenda.values[0],
                                   df_venda.idVendedor.values[0], df_venda.cpfCliente[0], df_venda.idCarro[0])
        # Exibe os atributos da nova venda
        print(nova_venda.to_string())
        # Retorna o objeto novo_pedido para utilização posterior, caso necessário
        return nova_venda

    def atualizar_venda(self) -> VendaVeiculo:
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        #Lista as vendas para serem alteradas
        '''def listar_vendas(self, oracle:OracleQueries, need_connect:bool=False):
        query = """
                select vend.idvenda,
                vend.valorvenda,
                vend.datavenda,
                vend.idvendedor,
                vend.cliente,  
                vend.veiculo  
                from venda vend
                inner join clientes
                on vend.cliente = c.cpfCliente
                inner join veiculos
                on vend.veiculo = veic.idCarro 
                order by vend.idvenda
                """
        if need_connect:
            oracle.connect()
        print(oracle.sqlToDataFrame(query))''' 

        # Solicita ao usuário o código da venda a ser alterado
        idVenda = int(input("Insira o código da Venda que irá alterar: "))        

        # Verifica se a venda existe na base de dados
        if not self.verifica_existencia_venda(oracle, idVenda):

            # Lista os clientes existentes para inserir na venda
            self.listar_clientes(oracle)
            novo_cpfCliente = str(input("Digite o novo número do CPF do Cliente: "))

            Cliente = self.valida_cliente(oracle, novo_cpfCliente)
            if Cliente == None:
                return None
          #  else:
           #     oracle.write(f"update VendaVeiculo set cpfCliente = '{novo_cpfCliente} where cpfCliente")

            # Lista os veiculos existentes para inserir na venda
            self.listar_veiculos(oracle)
            novo_idCarro = str(input("Digite o novo codigo do Veiculo: "))
            Veiculo = self.valida_veiculo(oracle, novo_idCarro)
            if Veiculo == None:
                return None
            else:
                oracle.write(f"update VendaVeiculo set idCarro = '{novo_idCarro} where cpfCliente = {idVenda}")

            #Solicita ao usuario o novo valor da venda
            novo_valorVenda = input("Informe o valor da venda: ")
            #atualiza o valor da venda
            oracle.write(f"update VendaVeiculo set valorVenda = '{novo_valorVenda} where idVenda = {idVenda}")
            #Solicita ao usuario o novo id do vendedor
            novo_idVendedor = input("Informe o id do vendedor: ")
            #atualiza o id do vendedor da venda
            oracle.write(f"update VendaVeiculo set idVendedor = '{novo_idVendedor} where idVenda = {idVenda}")
            # Atualiza a data da venda
            nova_dataVenda = input("informe a nova data da venda: ")
            #atualiza nova data da venda
            oracle.write(f"update VendaVeiculo set dataVenda = '{nova_dataVenda} where idVenda = {idVenda}")
            # Recupera os dados da nova venda criada transformando em um DataFrame
            df_venda = oracle.sqlToDataFrame(f"select VendaVeiculos  idVenda, valorVenda, dataVenda, idVendedor, cpfCliente, idCarro from VendaVeiculo where idVenda = {idVenda}")
            # Cria um novo objeto venda
            venda_atualizada = VendaVeiculo(df_venda.idVenda.values[0], df_venda.valorVenda.values[0], df_venda.dataVenda.values[0], df_venda.idVendedor.values[0], df_venda.cpfCliente[0], df_venda.idCarro[0])
            # Exibe os atributos da nova venda
            print(venda_atualizada.to_string())
            # Retorna o objeto venda_atualizado para utilização posterior, caso necessário
            return venda_atualizada
        else:
            print(f"O id {idVenda} não existe.")
            return None

    def excluir_venda(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        # Solicita ao usuário o código do produto a ser alterado
        idVenda = int(input("ID da venda que deseja exclir: "))        

        # Verifica se o produto existe na base de dados
        if not self.verifica_existencia_venda(oracle, idVenda):            
            # Recupera os dados do novo produto criado transformando em um DataFrame
            df_venda = oracle.sqlToDataFrame(f"select VendaVeiculos  idVenda, valorVenda, dataVenda, idVendedor, cpfCliente, idCarro from VendaVeiculo where idVenda = {idVenda}")
            #Cliente = self.valida_cliente(oracle, df_venda.idCliente.values[0])
            #Veiculo = self.valida_veiculo(oracle, df_venda.idCarro.values[0])
            
            opcao_excluir = input(f"Tem certeza que deseja excluir o pedido {idVenda} [S ou N]: ")
            if opcao_excluir.lower() == "s":
                print("Atenção, caso a venda possua itens, também serão excluídos!")
                opcao_excluir = input(f"Tem certeza que deseja excluir o pedido {idVenda} [S ou N]: ")
                if opcao_excluir.lower() == "s":
                    # Revome o produto da tabela
                    oracle.write(f"delete from VendaVeiculo where idVenda = {idVenda}")
                    print("Venda removida com sucesso!")
                    oracle.write(f"delete from VendaVeiculo where idVenda = {idVenda}")
                    # Cria um novo objeto Venda para informar que foi removido
                    venda_excluida = VendaVeiculo(df_venda.idVenda.values[0], df_venda.valorVenda.values[0], df_venda.dataVenda.values[0], df_venda.idVendedor.values[0], df_venda.cpfCliente[0], df_venda.idCarro[0])
                    # Exibe os atributos do produto excluído
                    print("Venda Removida com Sucesso!")
                    print(venda_excluida.to_string())
        else:
            print(f"O id {idVenda} não existe.")

    def verifica_prevenda(self, oracle:OracleQueries, cpfCliente:int=None, idVeiculo:int= None, idVenda:bool=False ) -> bool:
        df_venda = oracle.sqlToDataFrame(f"select idVenda from VendaVeiculo where cpfCliente and idVeiculo  = {idVenda}")
        return df_venda.empty
    
    def verifica_existencia_venda(self, oracle:OracleQueries, idVenda:int=None) -> bool:
        # Recupera os dados do novo pedido criado transformando em um DataFrame
        df_venda = oracle.sqlToDataFrame(f"select idVenda, dataVenda from Venda where idVenda = {idVenda}")
        return df_venda.empty

    def listar_clientes(self, oracle:OracleQueries, need_connect:bool=False):
        query = """
                select c.cpfCliente,
                c.idCliente,
                c.nome,
                c.email,
                c.telefone,
                c.endereco     
                from clientes c
                order by c.nome
                """
        if need_connect:
            oracle.connect()
        print(oracle.sqlToDataFrame(query))

    def listar_veiculos(self, oracle:OracleQueries, need_connect:bool=False):
        query = """
                select veic.idCarro,
                veic.modelo,
                veic.cor,
                veic.anoCarro,
                veic.chassiCarro,
                veic.tipoCambio,
                veic.fabricante
                from veiculos veic
                order by veic.modelo
                """
        if need_connect:
            oracle.connect()
        print(oracle.sqlToDataFrame(query))


    def valida_cliente(self, oracle:OracleQueries, cpfCliente:str=None) -> Cliente:
        if self.ctrl_cliente.verifica_existencia_cliente(oracle, cpfCliente):
            print(f"O CPF {cpfCliente} informado não existe na base.")
            return None
        else:
            oracle.connect()
            # Recupera os dados do novo cliente criado transformando em um DataFrame
            df_cliente = oracle.sqlToDataFrame(f"select cpfCliente, idCliente, nome, email, telefone, endereco from clientes where cpfCliente = '{cpfCliente}'")
            # Cria um novo objeto cliente
            cliente = Cliente(df_cliente.cpfCliente.values[0], df_cliente.idCliente.values[0], df_cliente.nome.values[0], df_cliente.email.values[0], 
                              df_cliente.telefone.values[0], df_cliente.endereco.values[0])
            return cliente

    def valida_veiculo(self, oracle:OracleQueries, idCarro:str=None) -> Veiculo:
        if self.ctrl_veiculo.verifica_existencia_veiculo(oracle, idCarro):
            print(f"O ID {idCarro} informado não existe na base.")
            return None
        else:
            oracle.connect()
            # Recupera os dados de uma nova venda criada transformando o em um DataFrame
            df_veiculo = oracle.sqlToDataFrame(f"select idCarro, novo_modelo, nova_cor, novo_ano, novo_chassiCarro, novo_tipoCambio, novo_fabricante from veiculos where idCarro = {idCarro}")
            # Cria um novo objeto venda
            veiculo = Veiculo(df_veiculo.idCarro.values[0], df_veiculo.modelo.values[0], df_veiculo.cor.values[0], df_veiculo.anoCarro.values[0], df_veiculo.chassiCarro.values[0],
                                         df_veiculo.tipoCambio.values[0], df_veiculo.fabricante.values[0], )
            return veiculo
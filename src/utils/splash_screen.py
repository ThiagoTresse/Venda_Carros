from conexion.oracle_queries import OracleQueries
from utils import config

class SplashScreen:

    def __init__(self):
        # Consultas de contagem de registros - inicio
        self.qry_total_cliente = config.QUERY_COUNT.format(tabela="cliente")
        self.qry_total_veiculo = config.QUERY_COUNT.format(tabela="veiculo")
        self.qry_total_VendaVeiculo = config.QUERY_COUNT.format(tabela="VendaVeiculo")
        # Consultas de contagem de registros - fim

        # Nome(s) do(s) criador(es)
        self.created_by = "Luiz Guilherme Oliveira\n\t Marcela Silva\n\tThiago Tresse"
        self.professor = "Prof. M.Sc. Howard Roatti"
        self.disciplina = "Banco de Dados"
        self.semestre = "2023/2"

    def get_total_cliente(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Retorna o total de registros computado pela query
        return oracle.sqlToDataFrame(self.qry_total_cliente)["total_cliente"].values[0]

    def get_total_veiculo(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Retorna o total de registros computado pela query
        return oracle.sqlToDataFrame(self.qry_total_veiculo)["total_veiculo"].values[0]

    def get_total_VendaVeiculo(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Retorna o total de registros computado pela query
        print(oracle.sqlToDataFrame(self.qry_total_VendaVeiculo))
        return oracle.sqlToDataFrame(self.qry_total_VendaVeiculo)["total_vendaveiculo"].values[0]

    def get_updated_screen(self):
        return f"""
        ########################################################
        #                   SISTEMA DE VENDAS DE CARROS                     
        #                                                         
        #  TOTAL DE REGISTROS:                                    
        #      1 - CLIENTES:         {str(self.get_total_cliente()).rjust(5)}
        #      2 - VEICULOS:         {str(self.get_total_veiculo()).rjust(5)}
        #      3 - VENDAS:           {str(self.get_total_VendaVeiculo()).rjust(5)}
        #     
        #  CRIADO POR: {self.created_by}
        #
        #
        #
        #  PROFESSOR:  {self.professor}
        #
        #  DISCIPLINA: {self.disciplina}
        #              {self.semestre}
        ########################################################
        """
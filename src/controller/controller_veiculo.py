from model.veiculos import Veiculo
from conexion.oracle_queries import OracleQueries

class Controller_veiculo:
    def __init__(self):
        pass
        
    def inserir_veiculo(self) -> Veiculo:
        ''' Ref.: https://cx-oracle.readthedocs.io/en/latest/user_guide/plsql_execution.html#anonymous-pl-sql-blocks'''
        
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        # Solicita ao usuario o novo id do veiculo 
        idCarro = input("idCarro (Novo): ")

        if self.verifica_existencia_idCarro(oracle, idCarro):
            # Solicita ao usuario o novo modelo do veiculo
            modelo = input("modelo (Novo): ")
            # Solicita ao usuario a cor do veiculo
            cor = input("cor (Novo): ")
            # Solicita ao usuario o ano do veiculo
            anoCarro = input("ano (Novo): ")
            # Solicita ao usuario o chassi do veiculo
            chassiCarro = input("chassi (Novo): ")
            # Solicita ao usuario o tipo de cambio do veiculo
            tipoCambio = input("tipo de cambio (Novo): ")
            # Solicita ao usuario o fabricante do veiculo
            fabricante = input("fabricante do carro (Novo): ")
            # Insere e persiste o novo veiculo
            oracle.write(f"insert into veiculos values ('{idCarro}', '{modelo}', '{modelo})', '{cor}', '{anoCarro}', '{chassiCarro}', '{tipoCambio}', '{fabricante}' ")
            # Recupera os dados do novo veiculo criado transformando em um DataFrame
            df_veiculo = oracle.sqlToDataFrame(f"select idCarro, modelo from veiculos where idCarro = '{idCarro}'")
            # Cria um novo objeto Veiculo
            novo_Veiculo = Veiculo(df_veiculo.idCarro.values[0], df_veiculo.modelo.values[0], df_veiculo.cor.values[0],
                            df_veiculo.anoCarro.values[0], df_veiculo.chassiCarro.values[0], df_veiculo.tipoCambio.values[0], df_veiculo.fabricante.values[0])
            # Exibe os atributos do novo veiculo
            print(Veiculo.to_string())
            # Retorna o objeto novo_veiculo para utilização posterior, caso necessário
            return novo_Veiculo
        else:
            print(f"O veiculo {idCarro} já está cadastrado.")
            return None

    def atualizar_veiculo(self) -> Veiculo:
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        # Solicita ao usuário o código do veiculo a ser alterado
        idCarro = int(input("Código do Veiulo que irá alterar: "))        

        # Verifica se o veiculo existe na base de dados
        if not self.verifica_existencia_veiculo(oracle, idCarro):
            # Solicita o novo modelo do veiculo
            novo_modelo = input("modelo (Novo): ")
            # Atualiza o modelo do veiculo existente
            oracle.write(f"update veiculos set modelo = '{novo_modelo}' where idCarro = {idCarro}")
            # Solicita ao usuario a nova cor do veiculo
            nova_cor = input("cor (Novo): ")
            # Atualiza a cor do veiculo existente
            oracle.write(f"update veiculos set cor = '{nova_cor}' where idCarro = {idCarro}")
            # Solicita ao usuario o novo ano do veiculo
            novo_ano = input("ano (Novo): ")
            # Atualiza o ano do veiculo existente
            oracle.write(f"update veiculos set anoCarro = '{novo_ano}' where cpf = {idCarro}")
            # Solicita ao usuario o novo chassi do veiculo
            novo_chassiCarro = input("chassi (Novo): ")
            # Atualiza o chassi existente
            oracle.write(f"update veiculos set chassiCarro = '{novo_chassiCarro}' where idCarro = {idCarro}")
            # Solicita o novo cambio do veiculo
            novo_tipoCambio = input("cambio (Novo): ")
            # Atualiza o cambio do veiculo existente
            oracle.write(f"update veiculos set cambio = '{novo_tipoCambio}' where idCarro = {idCarro}")
            # Solicita o novo fabricante do veiculo
            novo_fabricante = input("fabricante (Novo): ")
            # Atualiza o fabricante do veiculo existente
            oracle.write(f"update veiculo set fabricante = '{novo_fabricante}' where idCarro = {idCarro}")
            # Recupera os dados do novo produto criado transformando em um DataFrame
           ''' falta fazer essa parte do codigo: '''
           
            df_veiculo = oracle.sqlToDataFrame(f"select codigo_produto, descricao_produto from produtos where codigo_produto = {codigo_produto}")
            # Cria um novo objeto Produto
            produto_atualizado = Produto(df_produto.codigo_produto.values[0], df_produto.descricao_produto.values[0])
            # Exibe os atributos do novo produto
            print(produto_atualizado.to_string())
            # Retorna o objeto produto_atualizado para utilização posterior, caso necessário
            return produto_atualizado
        else:
            print(f"O código {codigo_produto} não existe.")
            return None

    def excluir_produto(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        # Solicita ao usuário o código do produto a ser alterado
        codigo_produto = int(input("Código do Produto que irá excluir: "))        

        # Verifica se o produto existe na base de dados
        if not self.verifica_existencia_produto(oracle, codigo_produto):            
            # Recupera os dados do novo produto criado transformando em um DataFrame
            df_produto = oracle.sqlToDataFrame(f"select codigo_produto, descricao_produto from produtos where codigo_produto = {codigo_produto}")
            # Revome o produto da tabela
            oracle.write(f"delete from produtos where codigo_produto = {codigo_produto}")            
            # Cria um novo objeto Produto para informar que foi removido
            produto_excluido = Produto(df_produto.codigo_produto.values[0], df_produto.descricao_produto.values[0])
            # Exibe os atributos do produto excluído
            print("Produto Removido com Sucesso!")
            print(produto_excluido.to_string())
        else:
            print(f"O código {codigo_produto} não existe.")

    def verifica_existencia_produto(self, oracle:OracleQueries, codigo:int=None) -> bool:
        # Recupera os dados do novo produto criado transformando em um DataFrame
        df_produto = oracle.sqlToDataFrame(f"select codigo_produto, descricao_produto from produtos where codigo_produto = {codigo}")
        return df_produto.empty
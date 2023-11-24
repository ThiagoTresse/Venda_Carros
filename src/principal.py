from utils import config
from utils.splash_screen import SplashScreen
from reports.relatorios import Relatorio
from controller.controller_cliente import Controller_Cliente
from controller.controller_veiculo import Controller_Veiculo
from controller.controller_vendaVeiculo import Controller_Venda

tela_inicial = SplashScreen()
relatorio = Relatorio()
ctrl_cliente = Controller_Cliente()
ctrl_veiculo = Controller_Veiculo()
ctrl_venda = Controller_Venda()

def reports(opcao_relatorio:int=0):

    if opcao_relatorio == 1:
        relatorio.get_relatorio_clientes()            
    elif opcao_relatorio == 2:
        relatorio.get_relatorio_veiculos()
    elif opcao_relatorio == 3:
        relatorio.get_relatorio_vendas()

def inserir(opcao_inserir:int=0):

    if opcao_inserir == 1:                               
        novo_cliente = ctrl_cliente.inserir_cliente()
    elif opcao_inserir == 2:
        novo_veiculo = ctrl_veiculo.inserir_veiculo()
    elif opcao_inserir == 3:
        nova_venda = ctrl_venda.inserir_venda()

def atualizar(opcao_atualizar:int=0):

    if opcao_atualizar == 1:
        relatorio.get_relatorio_clientes()
        cliente_atualizado = ctrl_cliente.atualizar_cliente()
    elif opcao_atualizar == 2:
        relatorio.get_relatorio_veiculos()
        veiculo_atualizado = ctrl_veiculo.atualizar_veiculo()
    elif opcao_atualizar == 3:
        relatorio.get_relatorio_vendas()
        vendas_atualizado = ctrl_venda.atualizar_venda()

def excluir(opcao_excluir:int=0):

    if opcao_excluir == 1:
        relatorio.get_relatorio_clientes()
        ctrl_cliente.excluir_cliente()
    elif opcao_excluir == 2:                
        relatorio.get_relatorio_veiculos()
        ctrl_veiculo.excluir_veiculo()
    elif opcao_excluir == 3:                
        relatorio.get_relatorio_vendas()
        ctrl_venda.excluir_venda()

def run():
    print(tela_inicial.get_updated_screen())
    config.clear_console(2)

    while True:
        print(config.MENU_PRINCIPAL)
        opcao = int(input("Escolha uma opção [1-5]: "))
        config.clear_console(1)
        
        if opcao == 1: # Relatórios
            
            print(config.MENU_RELATORIOS)
            opcao_relatorio = int(input("Escolha uma opção [0-3]: "))
            config.clear_console(1)

            reports(opcao_relatorio)

            config.clear_console(1)

        elif opcao == 2: # Inserir Novos Registros
            
            print(config.MENU_ENTIDADES)
            opcao_inserir = int(input("Escolha uma opção [1-3]: "))
            config.clear_console(1)

            inserir(opcao_inserir=opcao_inserir)

            config.clear_console()
            print(tela_inicial.get_updated_screen())
            config.clear_console()

        elif opcao == 3: # Atualizar Registros

            print(config.MENU_ENTIDADES)
            opcao_atualizar = int(input("Escolha uma opção [1-3]: "))
            config.clear_console(1)

            atualizar(opcao_atualizar=opcao_atualizar)

            config.clear_console()

        elif opcao == 4: # Excluir Registros

            print(config.MENU_ENTIDADES)
            opcao_excluir = int(input("Escolha uma opção [1-3]: "))
            config.clear_console(1)

            excluir(opcao_excluir=opcao_excluir)

            config.clear_console()
            print(tela_inicial.get_updated_screen())
            config.clear_console()

        elif opcao == 5:

            print(tela_inicial.get_updated_screen())
            config.clear_console()
            print("Agradecemos por utilizar o nosso sistema.")
            exit(0)

        else:
            print("Opção incorreta.")
            exit(1)

if __name__ == "__main__":
    run()
import os
import Queries

controle = ''

while True:
    os.system('clear')
    print("""   --- Create - Read - Update - Delete ---
                Selecione uma opção: 
                1 - Consultar os dados de todos;
                2 - Consultar os dados de apenas uma pessoa;
                3 - Inserir dados;
                4 - Alterar dados;
                5 - Deletar dados;
                0 - Parar a Execução""")
    controle = input("Digite aqui: ")

    if controle=='1':
        print("Consultar os dados de todos")
        Queries.selectAll()
        input()
    elif controle=='2':
        print("Consultar os dados de apenas uma pessoa")
        Queries.select(input("Digite o ID da pessoa: "))
        input()
    elif controle=='3':
        print("Inserir dados")
        Queries.insert(input("Nome: "), input("Idade: "), input("Profissão: "), input("Salário: "))
        input()
    elif controle=='4':
        print("Alterar dados")
        Queries.update(input("ID: "), input("Campo a ser alterado: "), input("Nova informação: "))
        input()
    elif controle=='5':
        print("Deletar dados")
        Queries.delete(input("ID: "))
        input()
    elif controle=='0':
        print("Parando a execução...")
        break
    else:
        print("Opção inválida!")
        input()

from time import sleep

lista_alunos = []

try:
    with open("alunos.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            nome, media = linha.strip().split(";")
            lista_alunos.append([nome, float(media)])
except FileNotFoundError:
    pass

while True:
    #MENU
    print("""
======= BOLETIM ESCOLAR =======

1 - Cadastrar aluno
2 - Listar alunos
3 - Ver aluno com maior média
4 - Mostrar média geral da turma
5 - Remover aluno
6 - Sair
""")

    try:
        opcao = int(input("Escolha: "))
    except ValueError:
        print("Digite uma opção válida.")
        continue
    #CADASTRO DE ALUNOS
    if opcao == 1:
        print("{:=^40}".format(" CADASTRO DE ALUNOS "))

        nome = input("Nome: ").strip()

        soma_notas = 0

        for i in range(2):
            while True:
                try:
                    nota = float(input(f"Digite a {i+1}ª nota: "))

                    if 0 <= nota <= 10:
                        soma_notas += nota
                        break

                    print("A nota deve estar entre 0 e 10.")

                except ValueError:
                    print("Digite um número válido.")

        media = soma_notas / 2

        lista_alunos.append([nome, media])

        print(f"Aluno cadastrado com média {media:.1f}")
    #LISTAR ALUNOS CADASTRADOS
    elif opcao == 2:
        print("{:=^40}".format(" LISTA DE ALUNOS "))

        if not lista_alunos:
            print("Nenhum aluno cadastrado.")
        else:
            resposta = None
            while resposta not in ["S", "N"]:
                resposta = str(input(
                    'Deseja listar em ordem alfabetica? [S/N]'
                )).upper().strip()[0]

                if resposta:
                    resposta = resposta[0]

                if resposta == "S":
                    for aluno in sorted(lista_alunos):
                        print(f'Nome: {aluno[0]} - Média: {aluno[1]:.1f}')

                elif resposta == "N":
                    for aluno in lista_alunos:
                        print(f"Nome: {aluno[0]} - Média: {aluno[1]:.1f}")
                elif resposta not in "SN":
                    print('Opção inválida...')
    #EXIBIR MELHOR ALUNO
    elif opcao == 3:
        print("{:=^40}".format(" MELHOR ALUNO "))

        if not lista_alunos:
            print("Nenhum aluno cadastrado.")
        else:
            maior = lista_alunos[0][1]
            melhor_aluno = lista_alunos[0][0]

            for aluno in lista_alunos:
                if aluno[1] > maior:
                    maior = aluno[1]
                    melhor_aluno = aluno[0]

            print(f"Aluno com a maior média: {melhor_aluno}")
            print(f"Média: {maior:.1f}")
    #MÉDIA GERAL DA TURMA
    elif opcao == 4:
        print("{:=^40}".format(" MÉDIA GERAL "))

        if not lista_alunos:
            print("Nenhum aluno cadastrado.")
        else:
            soma_medias = 0

            for aluno in lista_alunos:
                soma_medias += aluno[1]

            media_geral = soma_medias / len(lista_alunos)

            print(f"Média geral da turma: {media_geral:.1f}")
    #REMOVER ALUNO
    elif opcao == 5:
        print("{:=^40}".format(" REMOVER ALUNO "))

        if not lista_alunos:
            print("Nenhum aluno cadastrado.")
        else:
            nome_remover = input("Nome do aluno a remover: ").strip()

            encontrado = False

            for aluno in lista_alunos:
                if aluno[0].lower() == nome_remover.lower():
                    lista_alunos.remove(aluno)
                    encontrado = True
                    print("Aluno removido com sucesso.")
                    break

            if not encontrado:
                print("Aluno não encontrado.")
    #FINALIZA O PROGRAMA
    elif opcao == 6:
        with open("alunos.txt", "w", encoding="utf-8") as arquivo:
            for aluno in lista_alunos:
                arquivo.write(f"{aluno[0]};{aluno[1]}\n")

        print("Dados salvos.")
        print("Finalizando...")
        sleep(1)
        break

    else:
        print("Opção inválida.")

print("Volte sempre!")
## Estruturas de Controle de Fluxo

#Integre na solução anterior um fluxo de While que repita o fluxo até que o usuário insira as informações corretas

##### Solução

    # Inicializa as variáveis para o controle do loop

        #Solicita ao usuário inserir o seu nome, válido.


nome_valido = False
salario_valido = False
bonus_valido = False

while nome_valido is not True:
    try:
        nome = input("Digite o seu nome: ")
        if len(nome) == 0:
            raise ValueError("O nome não pode estar vazio.")
        elif any(char.isdigit() for char in nome):
            raise ValueError("O nome deve conter apenas letras.")
        else:
            nome_valido = True
            print("Nome válido: ", nome)
    except ValueError as e:
        print(e)

        # Solicita ao usuário que digite o valor do seu salário, válido.

while salario_valido is not True:
    try:
        salario = float(input("Insira o valor do seu salário: "))
        if salario <= 0:
            print("Insira um valor válido.")
            salario_valido = True
    except ValueError:
        print("Por favor, digite apenas números!")

        # Solicita ao usuário que digite o valor do bônus recebido, válido.

while bonus_valido is not True:
    try:
        bonus = float(input("Insira o valor do seu bônus: "))
        if bonus < 0:
            print("Por favor, digite um valor positivo para o bônus.")
    except ValueError:
        print("Entrada inválida para o bônus. Por favor, digite um número válido.")

        # exemplo simples de KPI.

bonus_recebido = 1000 + salario * bonus

        # Imprime as informações para o usuário.
print(f"{nome}, seu salário é R${salario:.2f} e seu bônus final é R${bonus_recebido:.2f}.")
## Estruturas de Controle de Fluxo

#Integre na solução anterior um fluxo de While que repita o fluxo até que o usuário insira as informações corretas

##### Solução

# Inicializa as variáveis para o controle do loop

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
            print("Nome válido: ", nome)
    except ValueError as e:
        print(e)

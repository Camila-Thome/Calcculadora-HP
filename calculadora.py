###
# Calculadora estilo HP
# Professor: Ariel Guareschi
# Aluno: Camila Queli Sockenski Thome
# Data: 13/05/2024
###

# Loop principal que faz com que o programa funcione de forma continua
while True:
    # Pede ao usuário que escolha uma operação ou encerre o programa
    comando = input(
        "Escolha um número ou uma operação:\n 1 - soma + \n 2- subtração - \n 3- multiplicação * \n 4 - divisão / \n ou 'X' para encerrar:\n ")
    
    # Processa a escolha do usuário
    match comando.upper():
        case '1':
            # Soma
            soma = 0.0  # Inicia a variável para armazenar a soma
            while True:
                num = input('Digite um número ou P para parar: ')
                if (num.upper() == 'P'):  # Usuário digita o 'P' quando quer encerrar a digitação dos algarismos
                    break
                soma += float(num)  # Adiciona o número na soma
            print(f'O resultado da soma é {soma}')  # Mostra o resultado da soma
        case '2':
            # Subtração
            subtração = None  # Inicia a variável para armazenar o resultado da subtração
            while True:
                num = input('Digite um número ou P para parar: ')
                if (num.upper() == 'P'):   # Usuário digita o 'P' quando quer encerrar a digitação dos algarismos
                    break
                if subtração is None:
                    subtração = float(num)  # Se for o primeiro número inserido, armazena-o como resultado inicial
                else:
                    subtração -= float(num)  # Subtrai o próximo número do resultado inicial
            if subtração is not None:
                print(f'O resultado da subtração é {subtração}')  # Mostra o resultado da subtração
        case '3':
            # Multiplicação
            multiplicação = 1.0  # Inicia a variável para armazenar o resultado da multiplicação
            while True:
                num = input('Digite um número ou P para parar: ')
                if (num.upper() == 'P'):   # Usuário digita o 'P' quando quer encerrar a digitação dos algarismos
                    break
                multiplicação *= float(num)  # Multiplica o número pelo resultado inicial
            print(f'O resultado da multiplicação é {multiplicação}')  # Mostra o resultado da multiplicação
        case '4':
            # Divisão
            divisão = None  # Inicia a variável para armazenar o resultado da divisão
            while True:
                num = input('Digite um número ou P para parar: ')
                if (num.upper() == 'P'):   # Usuário digita o 'P' quando quer encerrar a digitação dos algarismos
                    break
                if divisão is None:
                    divisão = float(num)  # Armazena o primeiro numero como resultado inical
                else:
                    if float(num) == 0:
                        print("Erro: Divisão por zero é indefinida. Ignorando este número.")  # Quando a divisão é por zero
                    else:
                        divisão /= float(num)  # Divide o resultado inicial pelo próximo número
            if divisão is not None:
                print(f'O resultado da divisão é {divisão}')  # Mostra o resultado da divisão
        case 'X':
            # Encerra o loop
            break

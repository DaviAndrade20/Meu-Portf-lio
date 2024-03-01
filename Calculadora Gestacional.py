while True:
    # Mensagem de boas-vindas
    input('''Olá. Gostaria de lhe dar as boas vindas à nossa calculadora gestacional.
  É um prazer ter você conosco e esperamos poder te ajudar.
  Pressione ENTER para continuar...''')

    # Verificar se o usuário já sabe sobre a idade gestacional e a data provável do parto
    answer = input('''Você já sabe o que é Idade Gestacional e a Data provável do parto? Digite Sim ou Não:''').strip()

    # Responder de acordo com a entrada do usuário
    if answer.lower() == 'sim':
        print('Pois bem, então vamos começar.')
    else:
        print('Ok, vou te explicar o que cada uma significa.')
        input('Pressione Enter')
        print('Idade Gestacional basicamente é o tempo de gravidez contado em dias e semanas, a partir do primeiro dia da última menstruação.')
        input('Pressione Enter')
        print('''A data provável do parto é a data em que o bebê provavelmente nascerá,
        levando em consideração que já tenham se passado 40 semanas após a data da última menstruação.''')
        print('Basicamente é isso.')

    # Aguardar a confirmação do usuário para continuar
    input('Pressione ENTER para continuar...')

    # Quebrar o loop após a execução
    break




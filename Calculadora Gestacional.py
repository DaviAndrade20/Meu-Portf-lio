from datetime import datetime, timedelta

# Função para validar a entrada de data
def obter_data(prompt):
    while True:
        try:
            # Solicita ao usuário a data no formato 'dd/mm/aaaa'
            data = input(prompt)
            # Tenta converter a data para o formato datetime
            data_convertida = datetime.strptime(data, "%d/%m/%Y")
            return data_convertida
        except ValueError:
            print("Erro: O formato da data está incorreto. Por favor, insira no formato dd/mm/aaaa.")

def calcular_idade_gestacional(dum, dhj):
    # Calcula a diferença entre a data de hoje e a data da última menstruação (DUM)
    idade_gestacional = dhj - dum
    semanas_gestacionais = idade_gestacional.days // 7
    dias_gestacionais = idade_gestacional.days
    return dias_gestacionais, semanas_gestacionais

def calcular_data_probavel_parto(dum):
    # A data provável do parto é 280 dias após a DUM (40 semanas)
    data_probavel_parto = dum + timedelta(days=280)
    return data_probavel_parto

# Início do programa
def main():
    while True:    
        # Mensagem de boas-vindas
        input('''Olá. Gostaria de lhe dar as boas-vindas à nossa calculadora gestacional. 
        É um prazer ter você conosco e esperamos poder te ajudar. 
        Pressione ENTER para continuar...''')

        # Verificar se o usuário já sabe sobre a idade gestacional e a data provável do parto
        answer = input('Você já sabe o que é Idade Gestacional e a Data provável do parto? Digite Sim ou Não: ').strip()

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

        # Coletar as datas do usuário
        dum = obter_data('Primeiramente, preciso que você digite a data da sua última menstruação (formato dd/mm/aaaa): ')
        dhj = obter_data('Agora, digite a data de hoje (formato dd/mm/aaaa): ')

        # Calcular a idade gestacional e a data provável do parto
        dias_gestacionais, semanas_gestacionais = calcular_idade_gestacional(dum, dhj)
        data_probavel_parto = calcular_data_probavel_parto(dum)

        # Exibir os resultados
        print(f'\nIdade gestacional: {dias_gestacionais} dias ({semanas_gestacionais} semanas)')
        print(f'Data provável do parto: {data_probavel_parto.strftime("%d/%m/%Y")}')

        # Perguntar se o usuário deseja realizar um novo cálculo
        continuar = input('Deseja realizar um novo cálculo? Digite "Sim" para continuar ou "Não" para sair: ').strip()
        if continuar.lower() != 'sim':
            break

    print('Obrigado por utilizar nossa calculadora gestacional!')

# Chama a função principal
if __name__ == "__main__":
    main()




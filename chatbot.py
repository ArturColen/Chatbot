import os

# Start the conversation with the user
def start():
    print('Olá! Sou o assistente virtual do Food from Brazil. Será um prazer te ajudar!')

    name = input(f'{os.linesep}Por gentileza, me informe o seu nome: ').capitalize()

    while True:
        answer = input(f'{os.linesep}{name}, selecione sobre o que deseja falar:{os.linesep}{os.linesep}[1] - Cardápio{os.linesep}[2] - Endereço{os.linesep}[3] - Horário de funcionamento{os.linesep}[4] - Reservas{os.linesep}[5] - Condições de aniversário{os.linesep}[6] - Eventos{os.linesep}[7] - Outros{os.linesep}{os.linesep}')
        
        process_answer(answer, name)

        proceed = input(f'Posso te ajudar em algo mais? (S/N) {os.linesep}').lower()

        if proceed == 's':
            continue
        else:
            print(f'{os.linesep}Muito obrigado pelo contato, {name}! Caso precise de algo mais é só chamar :)')
            break

# Check the alternative entered and show a response
def process_answer(answer, name):
    if answer == '1':
        print(f'{os.linesep}Esse é o link do nosso cardápio digital que te dá acesso ao nosso delicioso menu!{os.linesep}foodfrombrazil.com/cardapio/{os.linesep}')
    elif answer == '2':
        print(f'{os.linesep}Estamos localizados na Av. Paulista, 999 - Bela Vista, São Paulo - SP{os.linesep}Venha nos visitar, {name}!{os.linesep}')
    elif answer == '3':
        print(f'{os.linesep}Estes são nossos horários de funcionamento:{os.linesep}{os.linesep}Segunda a sexta-feira: 11h00 às 21h00{os.linesep}Sábado, domingo e feriado: 12h00 às 16h00{os.linesep}')
    elif answer == '4':
        print(f'{os.linesep}Que satisfação em saber que você quer reservar uma mesa com a gente, {name}! {os.linesep}{os.linesep}Faça sua reserva pelo link:{os.linesep}foodfrombrazil.com/reservas/{os.linesep}')
    elif answer == '5':
        print(f'{os.linesep}Que satisfação em saber que você deseja comemorar seu aniversário com a gente, {name}! {os.linesep}{os.linesep}O aniversariante da semana ganha um desconto de 10% no valor total da compra, além de uma deliciosa sobremesa da casa.{os.linesep}')
    elif answer == '6':
        print(f'{os.linesep}Temos condições especiais de eventos, happy hours e confraternizações.{os.linesep}{os.linesep}Para saber mais, acesse o link:{os.linesep}foodfrombrazil.com/eventos/{os.linesep}')
    elif answer == '7':
        print(f'{os.linesep}Desculpe por não poder te ajudar por aqui, {name}! {os.linesep}{os.linesep}Entre em contato conosco no e-mail contato@foodfrombrazil.com e iremos te ajudar por lá!{os.linesep }')
    else:
        print(f'{os.linesep}Não entendi o que você escreveu... Favor digitar uma alternativa válida.{os.linesep}')

# Execute the program
if __name__ == '__main__':
    start()
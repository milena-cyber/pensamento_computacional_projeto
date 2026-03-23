'''

CRUD
Barbearia

 Organizar e gerenciar clientes, agendamentos
 e serviços por meio das operações de cadastro,
 consulta, atualização e exclusão de dados.


 
 
'''


print('Hello world!')

# input('Precione o Enter para sair...')

nome_cliente = input('inserir seu nome:')


print(f'Olá, {nome_cliente}! Seja bem-vindo(a) a nossa barbearia!')



nome_conta = input ('Digite sua conta:')
print(f'{nome_conta} Correto agora entre com sua senha ')
input  ('Digite sua senha:')

nome_cliente = print ('Acesso permitido')
print ("escolha_menu")

print("\n=== BARBEARIA ===")
print("1. Cadastrar Cliente")
print("2. Agendar Serviço")
print("3. Meus Agendamentos")
print("4. Serviços e Preços")
print("5. Escolher Barbeiro")
print("6. Histórico e Pagamentos")
print("7. Avaliações")
print("8. Notificações")
print("0. Sair")

while True:

   escolha_menu = input("\nEscolha uma opção: ")

   if escolha_menu == '1':
   
      
    nome_cliente = input("Digite o nome do cliente: ")
    telefone_cliente = input("Digite o telefone do cliente: ")
    print("Cadastrando cliente...")

   elif escolha_menu =='2':

        print("perfil do cliente")  
        nome_cliente = input("nome completo do cliente:")
        nome_cliente = input("produtos que o cliente prefere:")

   elif escolha_menu == '3':

        print("Meus Agendamentos")
        nome_cliente = input("digite o nome do cliente para exibir agenda:")
        senha_cliente = input("digite a senha do cliente para confirmar o horário agendado:")

   elif escolha_menu == '4':

        print("Serviços e Preços")
        print("1. Corte de Cabelo: 30.00")
        print("2. Barba: 20.00")
        print("3. Corte + Barba: 45.00")
        print("4. Sobrancelha: 15.00")

   elif escolha_menu == '5':

        print("Escolher Barbeiro")
        print("1. Barbeiro Allan")
        print("2. Barbeiro Yuri")
        print("3. Barbeira Milena")
        
   elif escolha_menu == '6':

        print("Histórico e Pagamentos")
        nome_cliente = input("digite o nome e sobrenome do cliente para exibir histórico de serviço e pagamentos:")
        senha_cliente = input("digite a senha do cliente para confirmar o acesso ao histórico:")

   elif escolha_menu == '7':

        print("Avaliações")
        nome_cliente = input("digite o nome do barbeiro (ex: Barbeiro Allan) para avaliar o serviço:")
        avaliacao_cliente = input("digite sua avaliação (1 a 5 estrelas):")

   elif escolha_menu == '8':
        print("Notificações")
        nome_cliente = input("digite o nome do cliente para exibir notificações:")

   elif escolha_menu == '0':

        print("Saindo do sistema. Até logo!")
        break

   else:
        print("Opção inválida. Por favor, tente novamente.")





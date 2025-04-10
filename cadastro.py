nomes = []
idades = []
gastos = []

def cadastro():
    print("Para cadastrar um novo cliente, preencha os dados a seguir:")
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    gasto = float(input('Gasto: '))
    
    nomes.append(nome)
    idades.append(idade)
    gastos.append(gasto)
    
def exibi():
    p = input('Informe o nome do cliente que deseja consultar: ')
    for i in range(len(nomes)):
        if nomes[i] == p:
            print('\nDados do cliente:\n')
            print(f'Nome: {nomes[i]}')
            print(f'Idade: {idades[i]} anos')
            print(f'Gasto: {gastos[i]} reais')
            return 0
    print(f'Esse nome {p} não existe na lista!')
def balanco():
    media_idades = sum(idades)/len(idades)
    media_gastos = sum(gastos)/len(gastos)
    print(f'Os dados da sua base são:\n')
    print(f'O valor de idade media dos seus clientes são: {media_idades} anos')
    print(f'O valor medio de consumo na loja é de {media_gastos} reais')

print('Bem-vindo ao sistema de cadastro de clientes!')   
while True:
    print('\nInsira qual operação deseja realizar:\n')
    print('1 - Cadastrar novo cliente')
    print('2 - Buscar cliente na base')
    print('3 - Exibir dados da loja')
    print('4 - Sair do sistema')
    op = int(input('Operação: '))
    
    if op == 1:
        cadastro()
    if op == 2:
        exibi()
    if op == 3:
        balanco()
    if op == 4:
        break
    
print('\nSistema encerrado!')
print('Obrigado por usar nosso sistema!')
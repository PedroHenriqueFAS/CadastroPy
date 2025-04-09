nomes = []
idades = []
gastos = []

def cadastro():
    print("Para cadastrar um novo cliente, preencha os dados a seguir:")
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    gasto = input('Gasto: ')
    
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

for i in range(2):
    cadastro()
    exibi()
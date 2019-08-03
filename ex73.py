times = ('Santos', 'Palmeiras', 'Flamengo',
         'Internacional', 'Atlético MG', 'São Paulo',
         'Corinthians', 'Atlético PR', 'Botafogo',
         'Grêmio', 'Bahia', 'Goiás', 'Fortaleza',
         'Ceará', 'Vasco', 'Fluminense', 'Cruzeiro',
         'Chapecoense', 'CSA', 'Avaí')

op = 0

while op != 5:
    print("[ 1 ] 5 Primeiros colocados\n"
        "[ 2 ] 4 Últimos colocados\n"
        "[ 3 ] Times em ordem alfbética\n"
        "[ 4 ] Colocação de um time\n"
        "[ 5 ] Sair")
    print('=' * 30)
    op = int(input("Digite sua opção: "))

    if op == 1:
        print(times[:5])
    elif op == 2:
        print(times[-4:])
    elif op == 3:
        print(sorted(times))
    elif op == 4:
        time = str(input('Digite o nome do time: '))
        if time in times:
            print(f'{time} está na {times.index(time) + 1}ª posição')
        else:
            print('Time inválido tente novamente')
    elif op > 5 or op < 1:
        print('Opção inválida tente novamente')

nomes = [0] * 5
senhas = [0] * 5

for x in range(5):
    nomes[x] = input("Digite o nome do usuário: ")
    senhas[x] = input("Digite a senha do usuário: ")

tentativas_login = 0
while tentativas_login < 3:
    nomeLogin = input('Usuário: ')
    for i in range(5):
        if nomes[i] == nomeLogin:
            tentativas_login = 3
            print('Usuário encontrado!')
            for j in range(3): # 3 Tentativas para digitar a senha
                login_senha = input('Senha: ')
                if senhas[i] == login_senha:
                    print(f'Login realizado, bem vindo {nomeLogin}')
                    break
                else:
                    print('Senha invalida!')
    if tentativas_login < 3:
        print('Usuário invalido')
    tentativas_login += 1
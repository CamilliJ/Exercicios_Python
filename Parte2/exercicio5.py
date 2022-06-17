
usuario = input("Digite um usuário: ")
senha = input("Digite uma senha: ")

if len(usuario) < 12:
    print("O usuário deve conter mais que 12 caracteres!")
elif len(senha) < 8 and type(senha == string):
    print("A senha deve ser Númerica e conter mais que 8 caracteres!")
elif not senha.isalpha():
    print("A senha não pode conter caracteres especiais!")
else: 
    print("Conta criada com sucesso!")
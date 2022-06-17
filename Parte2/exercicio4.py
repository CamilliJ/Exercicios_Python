print(" ----- BEM VINDO(A) GUERREIRO(A)! -----")
print("Para começar a aventura, devemos escolher entre duas classes: MAGO ou GUERREIRO!")

classe = input("Qual você irá escolher?  \n")

if (classe == "MAGO" or classe == "GUERREIRO"):
    print("Exelente escolha!")
    nome = input("Qual o nome do seu Personagem? \n")

    if classe == "GUERREIRO":
        import random
        poder = random.randrange(5,10)

        print("\n \n | CLASSE : " , classe )
        print(" | NOME : " , nome )
        print(" | PODER : " , poder  )

        print("\n\n* Você a partir de agora tem 4 Opções: ")
        print("1 - Atacar  ")
        print("2 - Defender")
        print("3- Curar ")
        print("4- Descansar ")
        numeroacao = int(input("Digite o número correspondente a ação desejada: "))

        while numeroacao <1 or numeroacao >4 :
            print("Ação Inválida!")
            numeroacao = int(input("Digite o número correspondente a ação desejada: "))
        
        print("oi")

        

    if classe == "MAGO":
        import random
        poder = random.randrange(7,15)
        
else:
    print("Tente novamente na próxima!")
    
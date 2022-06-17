velocidade = input("Qual foi a velocidade? ")

if velocidade == "":
    print("Velocidade indisponivel!")
    import random
    aleatorio = random.randrange(1,120)
    valormulta = aleatorio * 7
    print("Por motivos governamentais a sua multa será de R$" , valormulta, "!")
else:
    velocidade = int(velocidade)

    if velocidade <=30:
    
        print("O veículo está muito lento, mude de mão imediatamente!")
    elif velocidade >= 90:
        exesso = velocidade - 90
        valormulta = exesso * 7
        print("O veículo está acima da velocidade permitida, a sua multa será de R$" , valormulta, "!")


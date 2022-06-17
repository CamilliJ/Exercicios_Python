totaleleitores = int(input("Qual o número de eleitores? "))
brancos = int(input("Quantos votaram nulo? "))
nulos = int(input("Quantos votaram branco? "))
validos =  totaleleitores - (brancos + nulos) 

porcbrancos = (brancos*100)/totaleleitores
porcnulos = (nulos*100)/totaleleitores
porcvalidos = (validos*100)/totaleleitores

print("O número total de eleitores é: " , totaleleitores)
print("Em relação ao número total de eleitores," , porcbrancos , "% deles votaram em branco.")
print("Em relação ao número total de eleitores," , porcnulos , "% deles votaram em nulo.")
print("Em relação ao número total de eleitores," , validos , "foram válidos.")


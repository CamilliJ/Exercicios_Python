idadeanos = int(input("Qual a sua idade em anos? "))
idademeses = int(input("Qual a sua idade em meses? "))
idadedias = int(input("Qual a sua idade em dias? "))

idadefinal = (idadeanos * 12 * 30) + (idademeses * 30) + idadedias

print("Idade total em dias: " , idadefinal)
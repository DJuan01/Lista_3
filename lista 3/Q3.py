codigo = input("Digite o codigo (V ou P):")
ValorV = 0
ValorP = 0
while (codigo == "V" or codigo== "P"):
    if codigo =="V":
        transacaoV = int(input("\n Informe a transacao a vista:"))
        ValorV = ValorV+transacaoV
    elif codigo =="P":
        transacaoP = int(input("\n Informe a transacao a vista:"))
        ValorP = ValorP+transacaoP
        
    codigo = input("\n Digite o codigo (V ou P) ")
    
ValorF = ValorP+ValorV
print(ValorV)
print(ValorP)
print(ValorF)





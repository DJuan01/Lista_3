Comprador= input("Digite que tipo de Comprador você é: Normal, Associado ou Parceiro:")
quant= int(input("Digite a quantidade:"))

if Comprador == "Normal":
    if (quant<=1000):
        valor= quant*1.1
        print(valor)
    elif(1000<quant<=5000):
        valor= quant*0.7
        print(valor)
    elif(5000<quant<=10000):
        valor= quant*0.4
        print(valor)
    elif (quant>10000):
        valor= quant*0.3
        print(valor)
if Comprador == "Associado":
    if(quant<=5000):
        valor= quant*0.7
        print(valor)
    elif(5000<quant<=10000):
        valor= quant*0.4
        print(valor)
    elif (quant>10000):
        valor= quant*0.3
        print(valor)
if Comprador == "Parceiro":
    if (quant<=1000):
        valor= quant*1.1
        valorf= valor*0.7
        print(valorf)
    elif(1000<quant<=5000):
        valor= quant*0.7
        valorf= valor*0.7
        print(valorf)
    elif(5000<quant<=10000):
        valor= quant*0.4
        valorf= valor*0.7
        print(valorf)
    elif (quant>10000):
        valor= quant*0.3
        valorf= valor*0.7
        print(valorf)
    


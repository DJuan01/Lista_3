quant_F = 0
quant_M= 0
pessoas= 0
sexo = int(input("Digite uma opção entre 1 para femenino e 2 para Masculino:"))
while sexo !=0 :
    if sexo == 1 :
        quant_F=quant_F+1
        pessoas +=1
    elif sexo == 2 :
        quant_M=quant_M+1
        pessoas +=1

        
    sexo = int(input("digite entre 1 e 2:"))
print(quant_M)
print(quant_F)
porc_F= quant_F/pessoas
porc_M=quant_M/pessoas
print(porc_F)
print(porc_M)
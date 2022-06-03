quant_T = 0
quant_B= 0
quant_R= 0
vinho_T= 0
vinho = int(input("Digite uma opção entre 1=(tinto); 2=(branco); 3=(Rosê):"))
while vinho !=0 :
    if vinho == 1 :
        quant_T=quant_T+1
        vinho_T +=1
    elif vinho == 2 :
        quant_B=quant_B+1
        vinho_T +=1
    elif vinho == 3 :
        quant_R=quant_R+1
        vinho_T +=1
        
    vinho = int(input("digite entre 1, 2 ou 3:"))
porc_T= quant_T/vinho_T
porc_B=quant_B/vinho_T
porc_R=quant_R/vinho_T
print(porc_T)
print(porc_B)
print(porc_R)
idade=1
while (idade>0):
    sexo= input("informe o sexo:")
    idade= int(input("informe a idade:"))
    escolaridade= int(input("informe a escolaridade:"))
    
    if (idade>0):
        if(sexo=="F" and idade<25 and escolaridade==2):
            print("recepcionista")
        elif(sexo=="M" and idade>40 and escolaridade==1):
            print("Servente")
        elif(idade<30 and escolaridade==3):
            print ("auxiliar de rh")
        else:
            print("NAo ha vagas")
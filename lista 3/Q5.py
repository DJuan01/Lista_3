num=1
contadorposi=0
contadornega=0
Nega= 0
Posi=0
while num!=0 :  
    num = int(input("insira números:"))
    
    if (num>0):
        Posi= Posi+ num
        contadorposi +=1
        FinalP= Posi/contadorposi
    if(num<0):
        Nega=Nega+num
        contadornega +=1
        FinalN= Nega/contadornega

print(Posi)
print(Nega)
Soma= FinalP+FinalN
print(Soma)
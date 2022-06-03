candidato1 = 0
candidato2= 0
candidato3=0
candidato4=0
nulo =0
branco=0
pessoas= 0
voto = int(input("Digite uma opção entre 1 e 6:"))
while voto !=0 :
    if voto == 1 :
        candidato1=candidato1+1
        pessoas +=1
    elif voto==2 :
        candidato2=candidato2+1
        pessoas +=1
    elif voto==3 :
        candidato3=candidato3+1
        pessoas +=1
    elif voto==4 :
        candidato4=candidato4+1
        pessoas +=1
    elif voto==5 :
        nulo=nulo+1
        pessoas +=1
    elif voto==6 :
        branco=branco+1
        pessoas +=1
        
    voto = int(input("digite entre 1 e 6:"))
Pnulos= nulo/pessoas
Pbranco= branco/pessoas
print(candidato1)
print(candidato2)
print(candidato3)
print(candidato4)
print(nulo)
print(branco)
print(Pnulos)
print(Pbranco)
    
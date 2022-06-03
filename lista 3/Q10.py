num = 0
idadeT=0
while num <1000 :
    num= int(input("Digite um numero:"))
    if num<=1000:
        
        idadeT= idadeT+ num
        
    elif num>1000:
        break
    
print(idadeT)
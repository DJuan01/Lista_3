contador=0
i=1
while i>0:
    idade= int(input("encreva sua idade:"))
    if idade>18:
        altura=float(input("Digite sua altura:"))
        if altura>1.6:
            contador +=1
        else:
                ("não elegivel")
    elif idade<18:
        break
print(contador)
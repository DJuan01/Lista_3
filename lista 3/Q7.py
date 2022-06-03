valorT=0
contador=0
valor=1
while valor != 0:
    valor = float(input("Digite numero par:"))
    if valor%2 ==0:
        contador +=1
        valorT=valorT+valor
    else: 
        print ("Isso é impar")

media= valorT/(contador-1)
print(media)

idadeT = 0
contador=0
idade= 1
while idade != 0 :
    idade= int(input("Digite sua idade:"))
    contador +=1 
    idadeT= idadeT+ idade
    
media= idadeT/(contador -1)
print(media)
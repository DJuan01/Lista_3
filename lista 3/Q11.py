n = 1
ma = None
me = None
soma_media=0
contador=0
while n>0:
    m = float(input("Digite um número: "))
    if m>0:
        ma = ma if ma != None and ma >  m else m
        me = me if me != None and me < m else m
        soma_media= soma_media+m
        contador +=1
    elif m<0:
        break
media_turma=soma_media/contador

print ('O maior valor digitado foi {} e o menor foi {}'.format(ma,me))
print(media_turma)
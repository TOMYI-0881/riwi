import time

lista = [None] * 192

for i in range(0, 100):

    for i in range(0, 192):
        if i == 0:
            lista[i] = "-"
        elif i == 191:
            lista[i] = "-"
        else:
            lista[i] = " "
     
    content =  "".join(lista)
    print(content)

    prueba = 2

    for i in range(0, 95):
        lista[i+1] = "-"
        lista [len(lista)-prueba] = "-"
        content =  "".join(lista)
        print(content)
        prueba+=1
        content =  "".join(lista)
        print(content)
        time.sleep(0.05)

    prueba = 96

    for i in range(95 ,0, -1):
        lista[i+1] = " "
        lista [prueba] = " "
        content =  "".join(lista)
        print(content)
        prueba+=1
        content =  "".join(lista)
        print(content)
        time.sleep(0.05)
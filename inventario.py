count = 0
process = 0

#We request inventory data using a while loop and use a try-catch 
#block to handle data errors and prevent the program from crashing
while count == 0:
    try:
        #We request user data
        if(process == 0):
            name = input("Nombre del Producto: ")
            process += 1
        elif(process == 1):
            price = float(input(f"precio del producto {name}: "))
            process += 1
        elif(process == 2):
            amount = int(input(f"que cantidad del Producto {name} quiere asignar: "))
            process += 1
            count += 1

    except ValueError:
        print("EL valor ingresado no es correcto")

#We calculate the total
total_price = amount * price

#add 0 to price
price_str = str(price)
count = 0
iteration = 0
for i in price_str:
    if(i == "."):
       count = 1
    elif(count == 1):
            iteration += 1

if(iteration == 1):
    price_str += "00"
elif(iteration == 2):
    price_str += "0"
elif(iteration == 0):

    price_str += "000"

#add 0 to total_price
total_price_str = str(total_price)
count = 0
iteration = 0
for i in total_price_str:
    if(i == "."):
       count = 1
    elif(count == 1):
            iteration += 1

if(iteration == 1):
    total_price_str += "00"
elif(iteration == 2):
    total_price_str += "0"
elif(iteration == 0):
    total_price_str += "000"

print()
print("-----------RECIBO GENERADO--------")
#We print it on the screen.
print(f"Nombre del producto: {name}\n"
      f"Precio unitario {price_str}\n"
      f"Cantidad {amount}\n"
      f"Costo total calculado {total_price_str}\n")
print("---------------------------------")

#while name!= None and product!= None and amount!= None:

#Añadir cadena a una variable
msg = "Hola"
msg += " "
msg += "User1"
print (msg)

#concatenar Strings
mensaje = "Hola"
espacio = " "
nombre = "User2"
print (mensaje + espacio + nombre)

#Concateniar string / number
n1 = 3
n2 = 12
suma = n1 + n2
suma = str(suma)
print("La suma de dos numeros es:" + suma)

#Busqueda metodo find()
mensaje1 = "Hola User3"
buscar = mensaje1.find("User3")
print (buscar)

#Busqueda con indices
mensaje2 =mensaje1
buscar2 = mensaje2[1:8]
print(buscar2)

#Comparacion
print (mensaje1 == mensaje2)

"""
Tipos de datos en python

Enteros y largos
    No tienen decimales
        int (enteros)
        long (largos)
Flotantes
    Decimales + -
        float
Complejos
    Parte real e imaginaria
        complex
Cadenas
    == String, textos
    Uso de:
        ""
        ''
Booleanos
    True o False
    Dato:
        bool
"""
#Entero / Largo
numInt = 15
print (numInt, type(numInt))

#Flotante
numFloat = 15.33
print (numFloat, type(numFloat))
#Declarar solo n decimales
numFloat2 = 12.32232134
print (round(numFloat2,2),type(numFloat))

#Complejo
numComplex = 15 + 1j
print (numComplex, type(numComplex))

#Cadena
cadena = "Esto es una cadena"
print (cadena, type(cadena))

#Booleano
boleano = 3==3
print (boleano, type(boleano))

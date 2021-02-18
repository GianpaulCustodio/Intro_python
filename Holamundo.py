#ejercicio1 For
#coleccion = {"Gp":22,"Spiderman":20,"Avengers":13}
#for clave,valor in coleccion.items():
#    print(f"{clave} -> {valor}")


#Ejercicio2-Intro
# a = int(input("Ingrese a->"))
# b = int(input("Ingrese b->"))
# suma=a+b
# print(f"La respuesta es {suma}")


#Intercambiar el valor entre 2 variables
# a = int(input("Ingrese a->"))
# b = int(input("Ingrese b->"))
# a,b=b,a
# print(f"valor de a-> {a}")
# print(f"valor de b-> {b}")


#Intercambiar el valor entre 3 variables
# a = int(input("Ingrese a->"))
# b = int(input("Ingrese b->"))
# c= int(input("Ingrese c->"))
# a,b,c=c,a,b
# print(f"valor de a-> {c}")
# print(f"valor de b-> {a}")
# print(f"valor de c-> {b}")


#Radio de circunferencia
# import math
# radio = float(input("Ingrese r ->"))
# longitud=2*math.pi*radio
# area=math.pi*radio*radio
# print(f"longitud -> {longitud}")
# print(f"area -> {area}")
# print("{0:.2f}".format(longitud)) #Para dos decimales


# #condicionales
# numero = int(input("ingrese un numero ->"))
# if numero>0:
#     print("Numero positivo")
# elif numero==0:
#     print("Numero es cero")
# else:
#     print("Numero negativo")


##condicionales multiples
# numero=int(input("Ingresa tu edad ->"))
# if numero>0:
#     if numero>=18 and numero<60:
#         input("Es mayor de edad")
#     elif numero>=60 and numero<105:
#         input("Es viejo")
#     elif numero>=105:
#         input("ERROR")
#     else:
#         input("Es menor de edad")
# elif numero==0:
#     print("Numero es cero")
# else:
#     input("El numero debe ser positivo")


# #Determinar si es una vocal o no
# letra=input("Ingrese una letra: ").lower() #Transforma la mayuscula a minuscula .... upper es para mayuscula a minuscula
# if letra=='a' or letra=='e' or letra=='i' or letra=='o' or letra=='u':
#     print("Es una vocal")
# else:
#     print("NO es una vocal")


# #Calculadora  s r m d
# letra = input("Ingrese la operación: ").lower()
# if letra=='s':
#     s1=int(input("1er número: "))
#     s2=int(input("2do número: "))
#     print(s1+s2)
# elif letra=='r':
#     r1=int(input("1er número: "))
#     r2=int(input("2do número: "))
#     print(r1-r2)
# elif letra=='m':
#     m1=int(input("1er número: "))
#     m2=int(input("2do número: "))
#     print(m1*m2)
# elif letra=='d':
#     d1=int(input("1er número: "))
#     d2=int(input("2do número: "))
#     print(d1/d2)
# else:
#     print("Ingrese un caracter correcto")


# #Menu de opciones
# inicial=100
# letra=int(input("Ingrese la opción: "))
# if letra==1:
#     adicional=int(input("Monto adicional: "))
#     adicional+=inicial
#     print(f"Saldo actual: {adicional}")
# elif letra==2:
#     retiro=int(input("Monto a retirar: "))
#     if retiro>inicial:
#         print("Excede al saldo inicial")
#     else:
#         retiro=inicial-retiro
#         print(f"Saldo actual: {retiro}")
# elif letra==3:
#     print(f"Saldo actual: {inicial}")


# Listas
# lista=[2,3,8,5,3,7,4,-1,-3,0]
# print(lista[4]) #Un elemento
# print(lista[0:4]) #Inicio->Fin
# lista.sort(reverse=True) #ordenar descendente
# lista.sort() #sirve para ordenar
# print(lista)


# a=int(input("a: "))
# b=int(input("b: "))
# lista=[a,b]
# if a in lista:
#     if a==0 and b==0:
#         print("Cero es neutro")
#     elif a==0 and b!=0:
#         if b%2==0:
#             print(f"Par: {b}")
#         else:
#             print("Ninguno es impar")
#     elif a!=0 and b==0:
#         if a%2==0:
#             print(f"Par: {a}")
#         else:
#             print("Ninguno es impar")
#     elif a!=0 and b!=0:
#         if a%2==0 and b%2==0:
#             print("Ambos numeros son pares")
#         elif (a%2==0 and b%2!=0):
#             print(f"Par: {a}")
#         elif a%2!=0 and b%2==0:
#             print(f"Par: {b}")
#         else:   
#             print("Ningún número es par")


# #Ingreso 5 elementos y elimino repetidos
# a=int(input("Primer número: "))
# b=int(input("Segundo número: "))
# c=int(input("Tercer número: "))
# d=int(input("Cuarto número: "))
# e=int(input("Quinto número: "))
# lista=[a,b,c,d,e]
# # #1era forma
# # conjunto=set(lista) #Se crea el conjunto
# # lista=conjunto
# #.........................................
# #2da forma
# lista=list(set(lista))
# print(lista)


#Ejercicio Listas
# primera_lista=["Gianpaul",12,14,16,"Spiderman"]
# segunda_lista=["Spike",11,14,12,"Hulk"]
#item1
#lista1=print(f"Primera lista: {primera_lista}")
#lista2=print(f"Segunda lista: {segunda_lista}")
#-----------------------------------------------
#item2 -Gp,16,spiderman
# l1=list(set(primera_lista))
# l2=list(set(segunda_lista))
# c1=set(primera_lista)
# c2=set(segunda_lista)
# item2=c1-c2
# a=list(item2)
# print(a)
#-----------------------------------------------
#item3 -Spike,11,Hulk
# c1=set(primera_lista)
# c2=set(segunda_lista)
# item2=c2-c1
# a=list(item2)
# print(a)
#-----------------------------------------------
#item4
# c1=set(primera_lista)
# c2=set(segunda_lista)
# item2=c1|c2
# a=list(item2)
# print(a)


#While
# import math
# n=int(input("Ingrese un número: "))
# while n<0:
#     print("Ingrese un número positivo: ")
#     n=int(input("Ingrese un número: "))
# print(f"Respuesta es: {(math.sqrt(n)):.2f}")

#imprimir 10 "Hola Mundo"
i=0
while i<10:
    print("Hola Mundo")
    i+=1
salir = True

while salir == True:

 print("Hola, bienvenido a la calculadora geometrica")

print("1. Circulo")
print("2. Rombo ")
print("3. Trapecio")
print("4. Pentagono rectangular")
print("5. Esfera")
print("6. Cilindro")
print("7. Cono")
print("8. Paralelepipedo")
print("9. Triangulo rectangulo")
print("10. salir")

opcion = int(input("Eliga una opcion: "))

if opcion == 1: 
   print("Elegiste circulo")
   radio = float(input("Ingresa el radio: "))
   area = 3.1416 * radio * radio
   print("El area del circulo es:", area)

elif opcion == 2:
   print("elegiste rombo")
   D = float(input("Diagonal mayor: "))
   d = float(input("diagonal menor: "))
   area = (D * d)/ 2
   print("El area del rombo es:", area)

elif opcion == 3:
    print("elegiste Trapecio")
    B = float(input("Base mayor: "))
    b = float(input("Base menor: "))
    h = float(input("Altura: "))
    area = ((B + b) * h) / 2
    print("El area del trapecio es:", area)

elif opcion == 4:
   print("Elegiste el pentagono regular")
   lado = float(input("Ingresa el lado: "))
   apotema = float(input("Ingresa la apotema: "))
   perimetro = 5 * lado
   area = (perimetro * apotema) / 2
   print("Area:", area)

elif opcion == 5:
   print("Elegiste esfera")
   radio =  float(input("ingresa el radio: "))
   volumen = (4/3) * 3.1416 * radio * radio
   print("Volumen:", volumen)
   print("Area:", area)

elif opcion == 6:
   print("elegiste cilindro")
   radio = float(input("ingrese el radio: "))
   altura = float(input("Ingrese la altura: "))
   volumen = 3.1416 * radio * radio * altura
   print("Volumen:", volumen)

elif opcion == 7:
    print("Elegiste cono")
    radio = float(input("Ingresa el radio: "))
    altura = float(input("Ingresa la altura: "))
    volumen = (3.1416 * radio * radio * altura) / 3
    print("Volumen:", volumen)

elif opcion == 8:
    print("Elegiste paralelepipedo")
    largo = float(input("Ingresa el largo: "))
    ancho = float(input("Ingresa el ancho: "))
    altura = float(input("Ingresa la altura: "))
    volumen = largo * ancho * altura
    print("Volumen:", volumen)

elif opcion == 9:
        print("Elegiste triangulo rectangulo")
        cateto1 = float(input("Cateto opuesto: "))
        cateto2 = float(input("Cateto adyacente: "))
        hipotenusa = (cateto1**2 + cateto2**2) ** 0.5
        area = (cateto1 * cateto2) / 2
        print("Hipotenusa:", hipotenusa)
        print("Area:", area)

elif opcion == 10:
     print("saliendo del programa")
     salir = True

else:
   print("opcion no valida")

print("Volviendo al menu...")


#Este programa calcula la ley de Ohm
print("Ley de Ohm")
print("Selecciona la opcion")
opcion=int(input("1=Voltaje, 2=Corriente, 3=Resistencia: "))
try:
    if opcion==1:
        resistencia=float(input("Ingresa la resistencia (Ohm): "))
        corriente=float(input("Ingresa la corriente (Amperios): "))
        voltaje=resistencia*corriente
        print("El voltaje es: ",voltaje,"Voltios")
    elif opcion==2:
        voltaje=float(input("Ingresa el voltaje (Voltios): "))
        resistencia=float(input("Ingresa la resistencia (Ohm): "))
        corriente=voltaje/resistencia
        print("La corriente es: ",corriente,"Amperios")
    elif opcion==3:
        voltaje=float(input("Ingresa el voltaje (Voltios): "))
        corriente=float(input("Ingresa la corriente (Amperios): "))
        resistencia=voltaje/corriente
        print("La resistencia es: ",resistencia,"Ohm")
    else:
        print("Opcion no valida")
except ValueError:
    print("Error: Entrada no valida. Por favor ingresa un numero.") 
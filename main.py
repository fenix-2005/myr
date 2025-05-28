
listn = []

while True:

    print ("-----Menu de notas-----")
    print ("1- Notas")
    print ("2- Promedio de notas")
    choice = int(input(""))

    if choice == 1:
        times = int(input("Ingrese cuantas notas va a calcular: "))

        for i in times:
            print (f"Ingrese la nota {i+1}")
            note = int(input(""))

    elif choice == 2:
        print
    else:
        print ("Datos ingresados no validos por favor reintente")

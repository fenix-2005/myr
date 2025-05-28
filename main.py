
listn = []

while True:

    print ("-----Menu de notas-----")
    print ("1- Notas")
    print ("2- Promedio de notas")
    choice = int(input(""))

    if choice == 1:
        times = int(input("Ingrese cuantas notas va a calcular: "))

        for i in range(times):
            print (f"Ingrese la nota {i+1}")
            note = int(input(""))
            listn.append(note)

    elif choice == 2:
        promedio = sum(listn) / len(listn)
        print (f"Su promedio es de {promedio}")

    else:
        print ("Datos ingresados no validos por favor reintente")

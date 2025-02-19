print("Hola, configure su nuevo PIN (debe tener 4 dígitos)")
# Todo el programa estara en un bucle, para si falla los 3 intentos del PIN, salga del bucle y tenga que iniciar de nuevo // no se funciones :(
while True:  
 #Sub-bucle de configuracion del PIN   
 while True:
    try:
        pin = int(input())
        if pin < 0:
            print("El numero debe ser positivo")
            continue         
        digits = len(str(pin))                      # Determina la cantidad de digitos del numero al convertirlo a una cadena string y determinar su extension
        if digits > 4 or digits < 4:
            print("El PIN debe tener 4 dígitos")
            continue
        break
    except ValueError:
        print("Por favor, introduce números válidos")

 print("\n Introduce tu nuevo PIN para continuar")  
 pin_counter = 0 # Contador de intentos de PIN
 pin_user = 0    # PIN que introduce el usuario para acceder

 while pin_user != pin: # Mientras que ambos PINs no sean iguales
    
    if pin_counter == 3: break # Si el contador de intentos llega a 3, romper el bucle.
    pin_user = int(input())

    if pin_user == pin:
        print("PIN correcto!")
        break
    elif pin_user != pin:
        print("PIN incorrecto")  
        pin_counter = pin_counter + 1
        continue

 if pin_counter == 3:           # Si el contador de intentos llego a 3, salir del bucle y se apaga el programa.
    print("Has introducido 3 veces mal el PIN, reiniciando sistema. Configura de nuevo")
    break
 
 print("\nFelicidades, por la creacion de tu cuenta has\n\tsido bonificado con $50!\n")

 cash = 50

 while True:
    print("\tMenú Principal\n1- Consultar saldo\n2- Retirar dinero\n3- Depositar dinero\n4- Salir")

    while True:
        try:
            choice = int(input())
            if choice < 1 or choice > 4:
                print("Introduce una de las opciones válidas de 1 al 4")
                continue
            break
        except ValueError:
            print("Introduce una opción válida")
    
    if choice == 1:
        print(f"Tu saldo es de ${cash}\n")
        continue
    
    elif choice == 2:
        print("Que cantidad de dinero deseas retirar? (Si ya no deseas retirar nada, escribe 0)")
        while True:
            try:
                cash_withdraw = int(input())
                if cash_withdraw > cash:
                    print("Saldo insuficiente, intentalo de nuevo\n")
                    continue
                elif cash_withdraw <= cash:
                    cash = cash - cash_withdraw
                    print(f"Has retirado ${cash_withdraw}")
                    print(f"Tu saldo actual es de ${cash}\n")
                    break
                elif cash_withdraw == 0:
                    print("Saliendo del menu de retirar\n")
                    break
                elif cash_withdraw <= 0:
                    cash = cash - (cash_withdraw)
                    print(f"Intentas depositar dinero?\nHas depositado ${-(cash_withdraw)}\nTu saldo actual es de ${cash}\n")
                    break
            except ValueError:
                print("Introduce un numero valido\n")

    elif choice == 3:
        print("Que cantidad de dinero deseas depositar? (Si no deseas depositar ya, escribe 0)")

        while True:
            try:
                cash_deposit = int(input())
                if cash_deposit == 0:
                    print("Saliendo del menu de deposito")
                    break
                elif cash_deposit >= 0:
                    cash = cash + cash_deposit
                    print(f"Has depositado ${cash_deposit}\nTu saldo actual es de ${cash}\n")
                    break
                elif cash_deposit < 0:
                    cash = cash + (cash_deposit)
                    print(f"Intentas retirar dinero?\nHas retirado ${-(cash_deposit)}\nTu saldo actual es ${cash}\n")
                    break
            except ValueError:
                print("Introduce un numero valido")
    
    elif choice == 4:
        break

 break

                          






            



    

  

    
    
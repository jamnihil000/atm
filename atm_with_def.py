cash = None

# Configuración del PIN del usuario.
def config_pin():
    print("Enter your PIN: ")
    while True:
        try:
            pin = int(input())
            if pin < 0:
                print("PIN must be greater than 0")
                continue
            digits = len(str(pin))
            if digits > 4 or digits < 4:
                print("PIN must be 4 digits")
                continue
            break
        except ValueError:
            print("Please, enter a valid numeric PIN")
    return pin                                       # Retorna el valor fuera de la funcion

# Autenticación del usuario con su PIN.
def auth(pin):

    print("Welcome to the auth system, introduce your credentials")
    pin_counter = 0                   # Contador de intentos de PIN
    pin_auth = None

    while pin_auth != pin:

        if pin_counter == 3: break
        pin_user = int(input())

        if pin_user == pin:
            break
        elif pin_user != pin:
            print("You have entered the wrong credentials")
            pin_counter += 1
            continue

    if pin_counter == 3:
        print("You have reached the 3 maximum attempts, configure a new PIN")
    elif pin_counter <3 :
        print("You have entered the correct credentials. You have been rewarded with $50!")

    global cash
    cash = 50

# Menu principal
def main_menu():
    print("Main Menu\n1- Balance\n2- Withdraw\n3- Deposit\n4- Exit")

    while True:
        try:
            choice = int(input())
            if choice < 1 or choice > 4:
                print("Please enter a valid 1 to 4 choice")
                continue
            break
        except ValueError:
            print("Please enter a valid choice")

    if choice == 1:
        consultar_saldo()
        return True

    elif choice == 2:
        withdrawn()
        return True

    elif choice == 3:
        deposit()
        return True

    elif choice == 4:
        return False

# Consultar saldo del usuario
def consultar_saldo():
    print(f"Your balance is ${cash}")

# Extraer dinero
def withdrawn():
    global cash
    print("What amount you want to withdraw?")
    while True:
        try:
            cash_withdraw = int(input())
            if cash_withdraw > cash:
                print("Saldo insuficiente, intentalo de nuevo")
                continue
            elif cash_withdraw <= cash:
                cash = cash - cash_withdraw
                print(f"Has retirado ${cash_withdraw}, Tu saldo actual es de ${cash}")
                break
            elif cash_withdraw == 0:
                print("Saliendo del menu de retirar\n")
                break
            elif cash_withdraw <= 0:
                cash = cash - (cash_withdraw)
                print(
                    f"Intentas depositar dinero?\nHas depositado ${-cash_withdraw} Tu saldo actual es de ${cash}")
                break
        except ValueError:
            print("Introduce un numero valido\n")

# Depositar dinero
def deposit():
    global cash
    print("What amount you want to deposit?")
    while True:
        try:
            cash_deposit = int(input())
            if cash_deposit == 0:
                print("Saliendo del menu de deposito")
                break
            elif cash_deposit >= 0:
                cash = cash + cash_deposit
                print(f"Has depositado ${cash_deposit} Tu saldo actual es de ${cash}")
                break
            elif cash_deposit < 0:
                cash = cash + (cash_deposit)
                print(f"Intentas retirar dinero?\nHas retirado ${-(cash_deposit)}Tu saldo actual es ${cash}")
                break
        except ValueError:
            print("Introduce un numero valido")

def atm_main():
    pin = config_pin()      # El valor pin es igual al retornado dentro de la funcion config_pin
    auth(pin)               # La funcion auth toma el valor de pin que provee la funcion config_pin
    while True:
        continuar = main_menu()
        if not continuar:
            break

atm_main()


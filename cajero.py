saldo  = 0.0
def consultar_saldo():
    print("Su saldo es:", saldo)


def retirar():
    global saldo
    dinero = float(input("¿Cuánto desea retirar? "))

    if dinero <= saldo:
        saldo = saldo - dinero
        print("Retiro exitoso")
        print("Nuevo saldo:", saldo)
    else:
        print("Saldo insuficiente")


def depositar():
    global saldo
    dinero = float(input("¿Cuánto desea depositar? "))

    saldo = saldo + dinero
    print("Depósito exitoso")
    print("Nuevo saldo:", saldo)


while True:

    print("\n--- CAJERO AUTOMÁTICO ---")
    print("1. Consultar saldo")
    print("2. depositar dinero")
    print("3. retirar dinero")
    print("4. Salir")

    opcion = int(input("Seleccione una opción: "))

    match opcion:
        case 1:
            consultar_saldo()

        case 2:
           depositar()

        case 3:
            retirar()

        case 4:
            print("Gracias por utilizar el cajero")
            break

        
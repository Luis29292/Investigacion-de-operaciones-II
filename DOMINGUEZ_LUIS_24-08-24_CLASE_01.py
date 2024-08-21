def ejercicio_01():
    nombre = input("Ingrese su nombre: ")
    print("Hola", nombre)

def ejercicio_02():
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    num3 = int(input("Ingrese el tercer número: "))

    resultado = (num1 + num2) * num3
    print("El resultado es:", resultado)

def ejercicio_03():
    dias = int(input("Ingrese el número de días: "))

    horas = dias * 24
    minutos = horas * 60
    segundos = minutos * 60

    print(f"El número de horas es: {horas}")
    print(f"El número de minutos es: {minutos}")
    print(f"El número de segundos es: {segundos}")

def ejercicio_04():
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))

    if num1 > num2:
        print("El primer número es más grande que el segundo.")
    else:
        print("El segundo número es más grande que el primero.")

def ejercicio_05():
    color = input("Ingrese un color: ")
    if color.lower() == "rojo": # Convierte el color a minúsculas
        print("A mí también me gusta el rojo.")
    else:
        print("A mí no me gusta el rojo.")

def ejercicio_06():
    num = int(input("Ingrese un número (1, 2 o 3): "))

    if num == 1:
        print("Gracias")
    elif num == 2:
        print("Bien hecho")
    elif num == 3:
        print("Correcto")
    else:
        print("Mensaje de error")

def ejercicio_07():
    total = 0
    while total <= 50:
        num = int(input("Ingrese un número: "))
        total += num
        print(f"El total es {total}.")


def ejercicio_08():
    num = int(input("Ingrese un número entre 10 y 20: "))

    if num < 10:
        print("El número es demasiado pequeño, intente de nuevo.")
    elif num > 20:
        print("El número es demasiado grande, intente de nuevo.")
    else:
        print("Gracias")

def ejercicio_09():
    compnum = 50
    num = int(input("Ingrese un número: "))

    if num < compnum:
        print("El número esperado es mayor, intente de nuevo.")
    elif num > compnum:
        print("El número esperado es menor, intente de nuevo.")
    else:
        print("Bien hecho, gracias")

def run():
    ejercicio_01()
    ejercicio_02()
    ejercicio_03()
    ejercicio_04()
    ejercicio_05()
    ejercicio_06()
    ejercicio_07()
    ejercicio_08()
    ejercicio_09()


if __name__ == '__main__':
    run()
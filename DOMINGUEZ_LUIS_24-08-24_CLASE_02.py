import math
def ejercicio_01(): #Solicita al usuario su primer nombre y retorna el número de caracteres que tiene su nombre (el largo de la cadena de texto).
    primer_nombre = input('Ingresa tu nombre: ')
    largo_nombre = len(primer_nombre)
    print(f"Tu nombre tiene {largo_nombre} caracteres.")

def ejercicio_02(): #Pide al usuario su primer nombre, y despues pide al usuario su segundo nombre. Una vez realizado eso, concatena estos dos strings con un espacio entre ellos y despues imprime.
    primer_nombre = input("Ingresa tu primer nombre: ")
    segundo_nombre = input("Ingresa tu segundo nombre: ")
    nombre_completo = primer_nombre + ' ' + segundo_nombre
    print(f"Tu nombre completo es: {nombre_completo}")

def ejercicio_03(): #Pregunta al usuairo por su primer nombre, si el largo del string es menor a 5, pide su apellido y concatena los strings sin espacio e imprime el texto en mayúsculas. Si el primer es igual o mayor a 5, imprime el string em minúsculas.
    primer_nombre = input("Ingresa tu primer nombre: ")
    if len(primer_nombre) < 5:
        apellido = input("Ingresa tu apellido: ")
        nombre_completo = primer_nombre + apellido
        print(nombre_completo.upper())
    else:
        print(primer_nombre.lower())

def ejercicio_04(): #Pregunta al usuario por su nombre e imprime su nombre 3 veces.
    name = input('Introduce tu nombre: ')

    for i in range(3):
        print(name)

def ejercicio_05(): #Pide al usuario su nombre y el número de veces que quieres que se repita su nombre.
    nombre = input("¿Cuál es tu nombre?: ")
    repticiones = int(input("¿Cuantas veces quieres que se repita  tu nombre?: "))

    for _ in range(repticiones):
        print(_)
        print(nombre)

def ejercicio_06(): #Pregunta al usuario a cuantas personas quiere invitar a su fiesta. Despues pide el nombre de los invitados; al final imprime todos los nombres por separado con la leyenda "[nombre] fue invitado". Hay una condición si la lista es mayor a 10, imprimir: "Son demasiados invitados". Nota: para guardar el nombre de los invitados puedes utilizar una lista
    num_invitados = int(input("¿A cuántas personas quieres invitar a tu fiesta?: "))
    invitados = []

    for _ in range(num_invitados):
        nombre = input("Ingresa el nombre del invitado: ")
        invitados.append(nombre)

    if len(invitados) > 10:
        print("Son demasiados invitados")
    else:
        for invitado in invitados:
            print(f"{invitado} fue invitado")

def ejercicio_07(): #Imprime el valor de pi con dos decimales.
    pi = math.pi
    print(f"{pi:.2f}")

def ejercicio_08(): #Pide al usuario un número con muchas decimales, mutiplique por dos, imprima, y luego imprima de nuevo, redondenado a dos digitos
    numero = float(input("Porfa ingresa un número con muchas decimales: "))
    resultado = numero * 2
    print(resultado)
    resultado_redondo = round(resultado, 2)
    print("El resultado redondo a dos digitos es: ", resultado_redondo)

def ejercicio_09():

    radio = float(input("Ingresa el radio del cilindro: "))
    profundidad = float(input("Ingresa la profundidad del cilindro: "))

    area_circulo = math.pi * radio**2
    volumen_total = round(area_circulo * profundidad, 3)

    print(f"El volumen total del cilindro es: {volumen_total}")

def ejercicio_10(): #Crea una lista vacia, despues añade a esa lista una seríe de frutas mediante un ciclo for, antes de comenzar el ciclo for, debes de decir cuantas frutas vas añadir (deben ser más de dos). Después imprime la lista. Una vez terminado el proceso pregunta al usuario que fruta desea eliminar de la lista porque ya la compró; elimine la fruta de la lista e imprima.
    frutas = []

    num = int(input("¿Cuantas frutas quiere agregar?: "))

    for i in range(num):
        fruta = input(f"Ingrese el nombre de la fruta {i+1}: ")
        frutas.append(fruta)
    print("Lista de frutas: ", frutas)

    fruta_eliminar = input("¿Qué fruta deseas eliminar porque ya la compraste?")

    if fruta_eliminar in frutas:
        frutas.remove(fruta_eliminar)
        print(f"La fruta eliminada es {fruta_eliminar}.")

    else:
        print(f"La {fruta_eliminar} no está en la lista.")

    print("Lista actualizada de frutas:", frutas)

def ejercicio_11(): #Cree una tupla con precios de productos, intente modificar la tupla y explique lo que sucede.
    tupla_01 = (41, 2, 3, 4)
    #tupla_01[0] = 20 #No se puede modificar una tupla, arroja error porque las tuplas son inmutables.

def ejercicio_12(): #Cree un diccionario e imprima la información mediante:
    diccionario_telefonos = {
        'Luis': 6436342634,
        'Maya': 5247838975,
        'Hazel': 6835685686,
        'Pancho': 7356835985,
    }

    for k, v in diccionario_telefonos.items():
        print(k, v)


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
    ejercicio_10()
    ejercicio_11()
    ejercicio_12()


if __name__ == '__main__':
    run()

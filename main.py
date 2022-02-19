from ListaOrdenada import ListaOrdenada
import entrada
import os
import time


def main():
    quiere_salir = False
    lista = ListaOrdenada()
    while not quiere_salir:
        print("1. Ingresar elemento")
        print("2. Sacar elemento")
        print("3. Mostrar lista")
        print("4. Mostrar longitud")
        print("5. Salir")
        opcion = entrada.leer_numero_positivo("Favor ingrese una opción: ")
        
        if opcion == 1:
            while True:
                try:
                    numero = int(input("\nIngrese el número a agregar a la lista: "))
                    lista.encolar(numero)
                except:
                    print("Valor invalido")
                    time.sleep(2)
                    os.system("cls")
                    continue
                else:
                    break    
        elif opcion == 2:
            if len(lista._ListaOrdenada) == 0:
                print("La lista esta vacía \n")
                time.sleep(2)
                os.system("cls")
            else:
                while True:
                    try:
                        var = 0
                        auxList = list.copy(lista._ListaOrdenada)
                        listLenght = len(auxList)
                        while var < listLenght:
                            print(f"La lista de elementos es la siguiente: \n")
                            print(f"Posicion [" + str(var) + "]: " + str(auxList.pop(0)))
                            var = var+1

                        indice = int(input("\nIngrese el índice del elemento a sacar: "))
                        lista.desencolar(indice)
                    except ValueError:
                        print("Valor invalido")
                        time.sleep(2)
                        os.system("cls")
                        continue
                    else:
                        break
        elif opcion == 3:
            lista.mostrarLista()

        elif opcion == 4:
            lista.__len__()

        elif opcion == 5:
            print("Gracias por usar el programa Lista Ordenada.")
            quiere_salir = True
        else:
            print("\nEsa no es una opción válida")
            os.system("pause")
            os.system("cls")

if __name__ == '__main__':
    main()
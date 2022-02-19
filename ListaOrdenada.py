from ntpath import join
import os
import time


class ListaOrdenada:

    def __init__(self):
        self._ListaOrdenada = []

    def encolar(self, numero):

        self._ListaOrdenada.append(numero)

        print(f"Ha agregado el número: {numero} \n")

        os.system("pause")
        os.system('cls')

    def desencolar(self, indice):

        if indice < len(self._ListaOrdenada) and indice > -1:
            num = self._ListaOrdenada.pop(indice)
            print(f"Ha sacado el número: " + str(num) +
            " de la posicion [" + str(indice) + "]\n")
        else:
            print("El indice indicado es invalido\n")

        os.system("pause")
        os.system('cls')  

    def __len__(self):
        print(
            f"La cantidad de números en la lista es {len(self._ListaOrdenada)} \n")

        os.system("pause")
        os.system('cls')  

    def mostrarLista(self):
        if len(self._ListaOrdenada) == 0:
            print("La lista esta vacía.")
        else:
            var = 0
            auxList = self._ListaOrdenada.copy()
            listLenght = len(auxList)
            print("\nLista: ")

            while var < listLenght:
                print(str(auxList.pop(0)))
                var = var+1

        print("\n")
        os.system("pause")
        os.system('cls')    

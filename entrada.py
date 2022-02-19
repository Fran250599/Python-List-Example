import os
def leer_numero_entero(mensaje_al_usuario, mensaje_de_error="Valor no valido"):
    ha_ingresado_valor_legal = False
    while ha_ingresado_valor_legal == False:
        try:
            valor_del_usuario = int(input(mensaje_al_usuario))
            ha_ingresado_valor_legal = True
        except ValueError:
            print(mensaje_de_error)
    return valor_del_usuario

def leer_numero_positivo(mensaje_al_usuario, mensaje_de_error="Valor no valido"):
    ha_ingresado_valor_legal = False
    while not ha_ingresado_valor_legal:
        valor_del_usuario = leer_numero_entero(mensaje_al_usuario, mensaje_de_error)
        if valor_del_usuario <= 0:
            print("Debe ser un número positivo")
        else:
            return valor_del_usuario
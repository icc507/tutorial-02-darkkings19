#Problema 2  / 9 ptos x4 pruebas / 36 puntos
#Concatenación de listas o tuplas
#---------------------------------------------------------------------------------
#Confeccione un programa que lea varios elementos y los entregue de manera inversa
#---------------------------------------------------------------------------------
#Ejemplo de entrada:
#         20 90 hola jiji 77
#La salida debe ser
#         (77, 'jiji', 'hola', 90, 20)
t = input().split()
mi_tupla = tuple(t)
tupla_invertida = mi_tupla[::-1]
tupla_invertida2 = ()

for elemento in tupla_invertida:
    elemento = elemento.strip()
    if elemento.isdigit():
        tupla_invertida2 += (int(elemento),)
    elif elemento:  # Agregar el elemento solo si no está vacío
        tupla_invertida2 += (elemento,)

print(tupla_invertida2)





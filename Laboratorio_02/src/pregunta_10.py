import os
import string

################## PREPROCESAMIENTO ##################

def a_mayusculas(texto):
  return texto.upper()

def eliminar_espacios_signos(texto):
  signosPuntuacion = [',',';',':','¿','?','!','¡','.']
  for item in signosPuntuacion:
    texto = texto.replace(item,'')
  texto = texto.replace(' ','').replace('\n','')
  return texto

def quitar_tildes(texto):
  reemplazosVocales = [
    ('á','a'),
    ('é','e'),
    ('í','i'),
    ('ó','o'),
    ('ú','u')
  ]
  for a1, a2 in reemplazosVocales:
    texto = texto.replace(a1, a2)
  return texto

############## FUNCIONES PARA EL CIFRADO ###############

def generar_alfabeto():
  lista_letras = list(string.ascii_uppercase)
  posicion = lista_letras.index('N')
  lista_letras = lista_letras[:posicion + 1] + ['Ñ'] + lista_letras[posicion + 1:]
  return lista_letras # 27 letras

def escribir_clave(texto, clave):
  tabla_cifrado = []
  clave_repetida = []
  texto_lista = list(texto)
  tabla_cifrado.append(texto_lista)
  index = 0
  for i in range(len(texto_lista)):
    if index == len(clave):
      index = 0
    clave_repetida.append(clave[index])
    index += 1
  tabla_cifrado.append(clave_repetida)
  return tabla_cifrado


####################### CIFRADO ########################

def cifrar(texto, clave, modulo):
  texto_claro = texto
  texto = eliminar_espacios_signos(texto)
  texto = quitar_tildes(texto)
  texto = a_mayusculas(texto)

  tabla_de_cifrado = escribir_clave(texto, clave)
  print(tabla_de_cifrado)
  print()
  pausa = str(input("\nPresione enter para regresar..."))

######################## MENUS ########################

def menu_modulo(texto,clave):
  while True:

    print("############ SELECCIÓN DEL MÓDULO ############\n\n\
1) Módulo 27\n\
2) Módulo 191 (ASCII)\n\
3) Regresar\n")

    opcion = int(input("Ingrese una opción(1-2-3): "))

    if opcion == 1:
      os.system("clear") 
      cifrar(texto, clave, 27)
    elif opcion == 2:
      os.system("clear") 
      # cifrar(texto,clave,191)
    elif opcion == 3:
      break
    os.system("clear") 


def menu():
  while True:

    print("\n############ CIFRADOR DE VIGNERE ############\n\n\
1) Ingresar texto por archivo\n\
2) Ingresar texto por consola\n\
3) Salir\n")

    opcion = int(input("Ingrese una opción(1-2-3): "))

    if opcion == 1:
      file_name = str(input("\nIngrese nombre del archivo (Ej: archivo.txt):\n"))
      clave = str(input("\nIngrese la clave de cifrado:\n"))
      os.system("clear") 
      with open("../txt/" + file_name, 'r', encoding = 'utf-8-sig') as entrada:
        texto = entrada.read()
        menu_modulo(texto, clave)
    elif opcion == 2:
      texto = str(input("\nIngrese el texto:\n"))
      clave = str(input("\nIngrese la clave de cifrado:\n"))
      os.system("clear") 
      menu_modulo(texto, clave)
    elif opcion == 3:
      break
    os.system("clear") 

######################## MAIN ########################

if __name__ == "__main__":
  menu()
  
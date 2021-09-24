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

def preprocesar(texto):
  texto_claro = texto
  texto = eliminar_espacios_signos(texto)
  texto = quitar_tildes(texto)
  texto = a_mayusculas(texto)
  return texto, texto_claro

############## FUNCIONES PARA EL CIFRADO ###############

def calcular_letra_cifrada(m, k, n):
  return (m + k) % n
  
####################### CIFRADO ########################

def cifrar(texto, clave, modulo):
  texto, texto_claro = preprocesar(texto)
  clave = a_mayusculas(clave)

  if modulo == 27:
    texto_cifrado = ""
    alfabeto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    ind = 0
    for car in texto:
      caracterText_index = alfabeto.index(car)
      caracterClav_index = alfabeto.index(clave[ind])
      posicion_cifra = calcular_letra_cifrada(caracterText_index, caracterClav_index, 27)
      texto_cifrado += alfabeto[posicion_cifra]
      ind += 1
      if ind == len(clave): 
        ind = 0
    print("TEXTO CIFRADO:\n",texto_cifrado,'\n')
  elif modulo == 191:
    texto_cifrado = ""
    alfabeto = [chr(i) for i in range(33, 225)]
    ind = 0
    for car in texto:
      caracterText_index = alfabeto.index(car)
      caracterClav_index = alfabeto.index(clave[ind])
      posicion_cifra = calcular_letra_cifrada(caracterText_index, caracterClav_index, 191)
      texto_cifrado += alfabeto[posicion_cifra]
      ind += 1
      if ind == len(clave): 
        ind = 0
    with open('HERALDOSNEGROS_unicode_8.txt', 'w') as output:
      output.write(texto_cifrado)
    print("TEXTO CIFRADO:\n",texto_cifrado,'\n')

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
      cifrar(texto,clave,191)
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
  
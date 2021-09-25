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
  texto = eliminar_espacios_signos(texto)
  texto = quitar_tildes(texto)
  return texto



####################### CIFRADO ########################

def vignere(texto, clave, modulo):
  # Para cifrar con módulo 27
  if modulo == 27:
    # Preprocesando texto plano
    texto = preprocesar(texto)
    texto = a_mayusculas(texto)
    clave = a_mayusculas(clave)
    texto_cifrado = ""
    alfabeto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    ind = 0
    for car in texto:
      caracterText_index = alfabeto.index(car)
      caracterClav_index = alfabeto.index(clave[ind])
      posicion_cifra = (caracterText_index + caracterClav_index) % 27
      texto_cifrado += alfabeto[posicion_cifra]
      ind += 1
      if ind == len(clave): 
        ind = 0
    with open('texto-cifrado_27.txt', 'w') as output:
      output.write(texto_cifrado)
    print("\n",texto_cifrado,'\n')

  # Para cifrar con módulo 191
  elif modulo == 191:
    # Solo quitamos espacios y saltos de línea
    texto = texto.replace(' ','').replace('\n','')
    clave = a_mayusculas(clave)
    texto_cifrado = ""
    # De esta lista se excluirá carácteres con \
    alfabeto = [chr(i) for i in range(33, 256)]
    ind = 0
    for car in texto:
      caracterText_index = alfabeto.index(car)
      caracterClav_index = alfabeto.index(clave[ind])
      posicion_cifra = (caracterText_index + caracterClav_index) % 191

      # Para no contar carácteres con \
      if posicion_cifra < 94:
        texto_cifrado += alfabeto[posicion_cifra]
      elif posicion_cifra >= 94:
        posicion_cifra += 32
        if posicion_cifra >= len(alfabeto):
          posicion_cifra = posicion_cifra % 191
          texto_cifrado += alfabeto[posicion_cifra]
        else:
          # En el peor de los casos podría volver a caer en un caracter /
          if posicion_cifra == 126 or posicion_cifra == 127 or posicion_cifra == 140:
            posicion_cifra %= 32
            texto_cifrado += alfabeto[posicion_cifra]
          else:
            texto_cifrado += alfabeto[posicion_cifra]
      ind += 1
      if ind == len(clave): 
        ind = 0
    with open('texto-cifrado_191.txt', 'w') as output:
      output.write(texto_cifrado)
    print("\n",texto_cifrado,'\n')
  return texto_cifrado
  pausa = str(input("\nPresione enter para regresar..."))


def frecuencies(texto, maxes = None):
    frecuencies_table = {}
    #text = open(texto, 'r').read().strip()
    #texto = preprocesar(texto)
    #texto = a_mayusculas(texto)
    #print(texto)
    #clave = a_mayusculas(clave)
    for char in texto:
        if not frecuencies_table.get(char):
            frecuencies_table[char] = 1
        else:
            frecuencies_table[char] += 1
    if maxes is None:
        return frecuencies_table
    else:
        five_maximum = sorted(frecuencies_table, key=frecuencies_table.get, reverse=True)[:5]
        return frecuencies_table, five_maximum
    pausa = str(input("\nPresione enter para regresar..."))
######################## MENUS ########################

def menu_modulo(texto,clave):
  while True:

    print("############ SELECCIÓN DEL MÓDULO ############\n\n\
1) Módulo 27\n\
2) Módulo 191 (ASCII)\n\
3) Frecuencias\n\n\
4) Regresar\n")

    opcion = int(input("Ingrese una opción(1-2-3): "))

    if opcion == 1:
      vignere(texto, clave, 27)

    elif opcion == 2:
      vignere(texto,clave,191)
    elif opcion == 3:
        #vignere(texto, clave, 27)
        texto_cifrado=vignere(texto, clave, 27)
        c = frecuencies(texto_cifrado)
        print(c)
        os.system("pause")
    elif opcion == 4:
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
      clave = str(input("\nIngrese la clave de cifrado (en mayúsculas):\n"))
      os.system("clear") 
      with open(file_name, 'r', encoding = 'utf-8-sig') as entrada:
        texto = entrada.read()
        menu_modulo(texto, clave)
    elif opcion == 2:
      texto = str(input("\nIngrese el texto:\n"))
      clave = str(input("\nIngrese la clave de cifrado (en mayúsculas):\n"))
      os.system("clear") 
      menu_modulo(texto, clave)

    elif opcion == 3:
      break
    os.system("clear") 

######################## MAIN ########################

if __name__ == "__main__":
  menu()
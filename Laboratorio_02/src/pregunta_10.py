import os

def a_mayusculas(texto):
  return texto.upper()

def eliminar_espacios_signos(texto):
  signosPuntuacion = [',',';',':','¿','?','!','¡','.']
  for item in signosPuntuacion:
    texto = texto.replace(item,'')
  texto = texto.replace(' ','').replace('\n','')
  return texto

def cifrar(texto, clave, modulo):
  texto_claro = texto
  texto = eliminar_espacios_signos(texto)
  texto = a_mayusculas(texto)
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
  
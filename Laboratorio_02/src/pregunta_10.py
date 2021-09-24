import os

def menu_modulo():
  while True:

    print("############ MENÚ ############\n\n\
1) Módulo 27\n\
2) Módulo 191 (ASCII)\n\
3) Regresar\n")

    opcion = int(input("Ingrese una opción(1-2-3): "))

    if opcion == 1:
      os.system("clear") 
      #mod_27()
    elif opcion == 2:
      os.system("clear") 
      #mod_191()
    elif opcion == 3:
      break
    os.system("clear") 


def menu():
  while True:

    print("\n############ CIFRADOR DE VIGNERE ############\n\n\
1) Seleccionar el módulo\n\
2) Salir\n")

    opcion = int(input("Ingrese una opción(1-2): "))

    if opcion == 1:
      os.system("clear") 
      menu_modulo()
    elif opcion == 2:
      break
    os.system("clear") 

if __name__ == "__main__":
  menu()
  
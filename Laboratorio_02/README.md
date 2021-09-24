# Laboratorio 02

## CIFRADO POLIALFABÉTICO

El código fuente fue desarrollado en Python.

### 10) Implementar un cifrador de Vignere, donde se pueda seleccionar el módulo, alfabeto módulo 27 o módulo 191 (ASCII)


```
def cifrar(texto, clave, modulo):
  
  # Preprocesando texto plano
  texto, texto_claro = preprocesar(texto)
  clave = a_mayusculas(clave)

  # Para cifrar con módulo 27
  if modulo == 27:
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
    print("TEXTO CIFRADO (modulo 27):\n\n",texto_cifrado,'\n')

  # Para cifrar con módulo 191
  elif modulo == 191:
    texto_cifrado = ""
    alfabeto = [chr(i) for i in range(33, 225)]
    ind = 0
    for car in texto:
      caracterText_index = alfabeto.index(car)
      caracterClav_index = alfabeto.index(clave[ind])
      posicion_cifra = (caracterText_index + caracterClav_index) % 191
      texto_cifrado += alfabeto[posicion_cifra]
      ind += 1
      if ind == len(clave): 
        ind = 0
    with open('texto-cifrado_191.txt', 'w') as output:
      output.write(texto_cifrado)
    print("TEXTO CIFRADO (modulo 191):\n\n",texto_cifrado,'\n')

  pausa = str(input("\nPresione enter para regresar..."))
```

<p align="center">
  <img src="src/pregunta_10/screens/main_menu.png"/>
</p>
<p align="center">
<img src="src/pregunta_10/screens/modulo_menu.png" />
</p>

#### Texto Plano

```
Hermoso es el cielo en el atardecer de tus ojos maravillosos
```

#### Resultado con módulo 27

```
JMVWDUWIDSNKMOZQMQOZCBECRGKICRGBYDDLWWWOTIZSZNWWZH
```

#### Resultado con módulo 191

```
jmvx}uwi~snkmpzqmrpzc|e}rgki}rg|y~}lwwxotiztznwwz
```

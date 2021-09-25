import re
from math import gcd

###################### DISTRIBUCIÓN ######################

# para obtener el caracter que cumple con la distribucion AEOS
def get_distibucion(texto):
    alfabeto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    mayor_frecuencias = {}
    # obteniendo frecuencias
    frecuencias = getFrecuencias(texto)
    for i in alfabeto:
        list = [j.start() for j in re.finditer(i, texto)]
        mayor_frecuencias[i] = len(list)
    for j in frecuencias:
        i = alfabeto.index(j)
        # buscamos con A E O R S
        if (mayor_frecuencias[alfabeto[i]] != 0 and  mayor_frecuencias[alfabeto[(i + 4) % 27]] != 0 and
            mayor_frecuencias[alfabeto[(i + 15) % 27]] != 0 and mayor_frecuencias[alfabeto[(i + 18) % 27]] != 0 and  # R
            mayor_frecuencias[alfabeto[(i + 19) % 27]] != 0):
            return j

###################### TRIGRAMAS ######################

# para obtener los trigramas
def trigrams(texto):
    list = [texto[ci - 3:ci] for ci in range(3, len(texto))]
    subs = set([texto[ci - 3:ci] for ci in range(3, len(texto))])
    trigramas = set()
    for sub in subs:
        cars = [m.start() for m in re.finditer(sub, texto)]
        if (len(cars) > 1):
            dist = []
            for ri in range(1, len(cars)):
                result = cars[ri] - cars[ri - 1]
                trigramas.add(result)
                dist.append(result)
    return trigramas

###################### CADENAS REPETIDAS ######################

# devuelve cadenas con una distancia determinada
def descomponer(texto, n):
    lista = []
    for i in range(n):
        lista.append("")
    for i in range(n):
        j = i
        while (j < len(texto)):
            lista[i] += texto[j]
            j += n
    return lista

###################### FRECUENCIAS ######################

# para obtener las frecuencias de cada caracter segun el lenguaje español
def getFrecuencias(texto):
    letras = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    nums = [12.53, 1.42, 5.68, 5.86, 13.68, 0.69, 1.01, 0.7, 6.25, 0.44, 0.01, 4.97,
    3.15, 6.71, 0.074, 8.68, 2.51, 0.88, 6.87, 7.98, 4.63, 3.93, 0.9, 0.02, 0.22, 0.9, 0.52]

    frecuencias = {}
    fr = {}
    for i in range(len(letras)):
        frecuencias[letras[i]] =nums[i]
    for i in texto:
        if i in fr: fr[i] += 1
        else: fr[i] = 1
    for j in fr:
        fr[j] *= frecuencias[j]
    fre_ordena =sorted(fr,key=fr.get,reverse=True)
    return fre_ordena

###################### MCD ######################

def calcular_mcd(nums):
    list_nums = list(nums)
    mcd = gcd(list_nums[0], list_nums[1])
    for i in range(2, len(list_nums)):
        factor = gcd(mcd, list_nums[i])
        if (factor != 1): mcd = factor
    return mcd

###################### DECIFRADO ######################

def decifrar(texto, clave):
    i = 0
    alfabeto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    texto_plano = ""
    for c in texto:
        caracterText_index = (alfabeto.index(c) - alfabeto.index(clave[i])) % 27
        texto_plano += alfabeto[caracterText_index]
        i += 1
        if i > len(clave) - 1: i = 0
    return texto_plano

###################### MAIN ######################

def main():
    texto = ""
    with open("texto_plano.txt") as input:
        texto = input.read()
    # eliminando saltos de linea
    texto = texto.replace('\n','')
    # hallando mcd
    mcd = calcular_mcd(trigrams(texto))
    listas = descomponer(texto, mcd)
    clave = ""
    for i in listas:
        clave += get_distibucion(i)

    cad = "Texto Descifrado:\n\n" + decifrar(texto, clave) +"\n\nLa clave de cifrado es: " + clave
    with open('texto-descifrado.txt', 'w') as output:
      output.write(cad)

if __name__ == '__main__':
    main()

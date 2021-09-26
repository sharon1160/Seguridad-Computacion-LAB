abc = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
texto = open("18.txt",encoding='utf-8')
linea = texto.read()
texto.close()

clave = 'UNODELOSMASGRANDESCRIPTOGRAFOS'

def descifrar(texto,clave):
    k=0
    s=0
    descifrado=''
    for i in texto:
        TamClave = len(clave)
        a = abc.find(i)
        if (k<TamClave):
            b= abc.find(clave[k])
            resta = (a-b)%27
            k=k+1 
        else:
            b= abc.find(descifrado[s])
            resta = (a-b)%27
            s=s+1
        descifrado = descifrado + abc[resta]
    print(descifrado)
    
descifrar(linea,clave)
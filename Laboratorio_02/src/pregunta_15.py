abc = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
texto = 'WPIXHVYYOSRTECSZBEEGHUUFWRWTZGRWUFSRIWESSXVOHAIHOHWWHCWHUZOBOZEAOYBMCRLTEYOTI'
clave = 'HIELO'


def descifrar(texto,clave):
    k=0;
    descifrado=''
    for i in texto:
        TamClave = len(clave)
        a = abc.find(i)
        if (k<TamClave):
            b= abc.find(clave[k])
            k=k+1
            if k == TamClave:
               k=0
        resta = (a-b)% 27
        descifrado = descifrado + abc[resta]
    print(descifrado)
                        
    
    
descifrar(texto,clave)

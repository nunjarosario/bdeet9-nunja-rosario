def contar_letras(oracion):
    conteo={}
    oracion= oracion.lower()
    for letra in oracion:
        if letra !="":
            if letra in conteo:
                conteo[letra]+=1
            else:
                conteo[letra]=1
    return conteo
print(contar_letras("Hola Mundo"))
 
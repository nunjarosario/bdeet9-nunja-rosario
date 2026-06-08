def contar_vocales(oracion):
    vocales="aeiou"
    conteo={vocal:0 for vocal in vocales}
    oracion= oracion.lower()
    for caracter in oracion:
       if caracter in conteo:
        conteo[caracter]+=1
    return conteo


print(contar_vocales("Hola Mundo"))  
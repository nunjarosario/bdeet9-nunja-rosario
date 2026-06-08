def todos_iguales(lista):
    if len(lista)==0:
        return True
    primer_elemento= lista[0]
    for elemento in lista:
        if elemento!= primer_elemento:
            return False
        return True
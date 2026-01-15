"""
Enunciado:

Implementa una función llamada find_max(lst) que encuentre el valor máximo en una
lista de números utilizando recursión. La función debe devolver el valor
máximo de la lista.

Parámetros:
    lst (List): lista de números enteros o flotantes

Ejemplo:
    Entrada:
    numbers_list = [1, 5, 2, 7, 3]
    find_max(numbers_list)

    Salida:
    7


Enunciat:

Implementa una funció anomenada find_max(lst) que trobi el valor màxim en una
llista de números utilitzant recursió. La funció ha de tornar el valor
màxim de la llista.

Paràmetres:
     lst (List): llista de nombres enters o flotants

Exemple:
     Entrada:
     numbers_list = [1, 5, 2, 7, 3]
     fid_max(numbers_list)

     Sortida:
     7

"""


def find_max(lst):
    # Write here your code
    if not isinstance(lst, list) or len(lst) == 0:
        raise("El parametro 'lst' debe ser una lista no vacia")
    
    for n in lst:
        if not isinstance(n, (int, float)) or isinstance(n, bool):
            raise("La lista debe contener solo numeros int o float")
        
    # caso base: si existe un solo elemento, este es el maximo
    if len(lst) == 1:
        return lst[0]
    
    # Maximo del resto - recursion
    max_rest = find_max(lst[1:])

    # Compara el primer con el resto
    return lst[0] if lst[0] > max_rest else max_rest


    pass


# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script
# Si vols provar el teu codi, descomenta les línies següents i executa l'script
# numbers_list = [1, 5, 2, 7, 3]
#print(find_max([1, 5, 2, 7, 3]))

""" Ejercicio 1 * Happy Numbers * Lambda.
OPTIMIZACIÓN: 1.b 
Se explora la posibilidad de que los 'seen_numbers' de 'is_happy()' sean devueltos y reingresados
a la función. De esta manera, el programa no tiene que empezar de nuevo a anotar los 'seen_numbers'.
Esto ahorra al programa de realizar cálculo innecesarios, sin embargo debe realizar operaciones extra 
de lectura y escritura sobre los sets, lo que no resulta en una optimización real para todos los casos.
Ver al final de este script un análisis de rendimiento.
Consigna:
    Hacer un programa que imprima los X primeros “happy numbers”.
"""

def pdi_function(number, power, base: int = 10):
    """Perfect digital invariant function.
        Realiza la suma de los dígitos de un número elevados a una potencia dada.
    
    Args:
        number: número al que se le aplicará la operación matemática.
        power: potencia a la que se elevan los dígitos del número.
        base (Opcional): base del sistema de numeración. Por defecto se usa base decimal.
    Returns:
        Devuelve un valor entero que es el resultado de la operación matemática.
    """
    total = 0
    while number > 0:
        total += pow(number % base, power)
        number = number // base
    return total

def is_happy(number: int, goal_value, power, seen_numbers):
    """Determina si el número especificado es un 'happy number'.
    
    Args:
        number: número del que se desea saber si es 'happy number'.
        goal_value: valor final al que debe llegar la operación para que se considere 'happy number'.
        power: exponente de la potencia que se aplica en 'pdi_function()'.
        seen_numbers: es un set que contiene los números que sabemos que no son happy_numbers ('unhappy_set')
    Returns:
        Devuelve un valor booleano que indica si el número es un 'happy number'.
        Devuelve el set 'new_seen_numbers' que contiene los números vistos por el programa en esta
        iteración añadidos al set que recibió ('seen_numbers')
    """
    new_seen_numbers = seen_numbers.copy() # copiamos el set en uno nuevo para que no lo sobreescriba
    while number != goal_value and number not in new_seen_numbers:
        new_seen_numbers.add(number)
        number = pdi_function(number, power)
    return number == goal_value , new_seen_numbers

def happy_numbers(n: int, goal_value: int=1, power: int=2):
    """ Imprime los n primeros 'happy numbers'.
    
    Args:
        n: cantidad de valores que queremos que se impriman.
        goal_value (Opcional): valor final al que debe llegar la operación para que se considere 'happy number'.
        power (Opcional): exponente de la potencia que se aplica en 'pdi_function()'.
    """

    unhappy_set = set()
    happy_list = []
    number = 1
    while len(happy_list) < n:
        if number in unhappy_set:
            number += 1
            continue
        else:
            boolean, number_set = is_happy(number, goal_value, power, unhappy_set)
            if boolean:
                happy_list.append(number)   # agregamos el numero a la lista de happy numbers
                                            # si boolean=True, el set 'number_set' se descarta
            else:
                unhappy_set = unhappy_set.union(number_set) # unimos el set de unhappy numbers 
                                                            #con el set number_set que recibimos
        number += 1

    print(happy_list)


""" 
    Ejemplo de uso "optimizado" para:

    >> happy_numbers(10, 1 , 2)
    [1, 7, 10, 13, 19, 23, 28, 31, 32, 44]
 
    Para medir la eficiencia utilizamos la utilidad 'time' de Linux:
    __________________________________________________________________________
    $ time python3 happy_numbers.py
    [1, 7, 10, 13, 19, 23, 28, 31, 32, 44]

    real	0m0,047s
    user	0m0,037s
    sys	    0m0,008s
    __________________________________________________________________________
    $ time python3 happy_numbers_opt1.py
    [1, 7, 10, 13, 19, 23, 28, 31, 32, 44]

    real	0m0,044s
    user	0m0,030s
    sys	0m0,014s
    __________________________________________________________________________

    Vemos como para este ejemplo de uso la eficiencia es levemente mayor en el programa "optimizado".
    Sin embargo, el programa se vuelve mucho más ineficiente a medida que aumentamos el número 'n' de 
    happy numbers que le pedimos y también si aumentamos la potencia que le pasamos.

    Aunque el resultado no es el esperado y no se puede considerar que el programa se haya optimizado,
    se presenta este intento para mostrar otro modo de encarar la solución del problema.

 
 """



happy_numbers(10, 1, 2)
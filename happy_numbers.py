"""
Ejercicio 1 * Happy Numbers
Hacer un programa que imprima los X primeros “happy numbers”.
"""

def pdi_function(number, power, base: int = 10):
    """Perfect digital invariant function."""
    total = 0
    while number > 0:
        total += pow(number % base, power)
        number = number // base
    return total

def is_happy(number: int, goal_value: int = 1, power: int=2) -> bool:
    """Determina si el número especificado es un 'happy number'.
    
    Args:
        number: número del que se desea saber si es 'happy number'.
        goal_value: valor final al que debe llegar la operación para que se considere 'happy number'.
        power: exponente de la potencia que se aplica en 'pdi_function()'.
    Returns:
        Devuelve un valor booleano que indica si el número es un 'happy number'.
    """
    seen_numbers = set()
    while number != goal_value and number not in seen_numbers:
        seen_numbers.add(number)
        number = pdi_function(number, power)
    return number == goal_value

def happy_numbers(n, goal_value: int=1, power: int=2):
    """ Imprime los n primeros 'happy numbers'.
    
    Args:
        n: cantidad de valores que queremos que se impriman.
        goal_value (Opcional): valor final al que debe llegar la operación para que se considere 'happy number'.
        power (Opcional): exponente de la potencia que se aplica en 'pdi_function()'.
    """
    happy_list = []
    number = 1
    while len(happy_list) < n:
        if is_happy(number, goal_value, power):
            happy_list.append(number)
        print(number)
        number += 1
    print(happy_list)


""" 
Ejercicio 1. Happy numbers.
Variación A. 
 """


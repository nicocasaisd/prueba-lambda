'''
Ejercicio 1 * Happy Numbers
Hacer un programa que imprima los X primeros “happy numbers”.
'''

def pdi_function(number, power, base: int = 10):
    """Perfect digital invariant function."""
    total = 0
    while number > 0:
        total += pow(number % base, power)
        number = number // base
    return total

def is_happy(number: int, goal_value: int = 1, power: int=2) -> bool:
    """Determine if the specified number is a happy number."""
    seen_numbers = set()
    while number != goal_value and number not in seen_numbers:
        seen_numbers.add(number)
        number = pdi_function(number, power)
    return number == goal_value

def happy_numbers(n, goal_value: int=1, power: int=2):
    happy_list = []
    number = 1
    while len(happy_list) < n:
        if is_happy(number, goal_value, power):
            happy_list.append(number)
        print(number)
        number += 1
    print(happy_list)



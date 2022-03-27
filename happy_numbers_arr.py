import numpy as np

number_arr = np.arange(4)


def pdi_function_arr(number_arr, power: int = 2, base: int = 10):

    total = np.zeros(number_arr.size, dtype=np.int32)
    while np.any(number_arr):
        total += pow(number_arr % base, power)
        number_arr = number_arr // base
    
    return total

def is_happy_arr(number_arr):

    for num in number_arr:
        seen_numbers = set()
        while num != 1 and num not in seen_numbers:
            seen_numbers.add(num)
            num = pdi_function_arr(number_arr, 2)

    return number_arr == 1

is_happy_arr(number_arr)

#total = pdi_function_arr(number_arr)
#print(total)
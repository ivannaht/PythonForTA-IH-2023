""" task 3_1"""
from helpers.custom_exceptions import BigNumberError
from helpers.logger import logger_with_arguments


def calculate_cubes_sum(numbers):
    """function for calculating cubes of integer numbers"""
    cubes_sum = 0
    for number in numbers:
        cubes_sum += pow(int(number), 3)
    return cubes_sum


@logger_with_arguments("logger for function",
                       "started", "finished")
def convert(str_main, n) -> str:
    """convert function for strings"""
    if not isinstance(n, int):
        raise TypeError("n must be integer number")
    if len(str_main) != 0 and n > len(str_main):
        raise BigNumberError(str_main, n)

    if n == 0:
        return ""

    count = len(str_main) // n
    first = 0
    last = n
    result = ""
    for i in range(0, count):
        result_str = str_main[first:last]
        result_list = list(str_main[first:last])
        if calculate_cubes_sum(result_list) % 2 == 0:
            result += result_str[::-1]
        else:
            result += result_str[1:] + result_str[0]
        first += n
        last += n
    return result


convert("123456987654", 6)

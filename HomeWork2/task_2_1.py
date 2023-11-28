from functools import reduce
from collections import Counter
from isort.sorting import sort


def stat(numbers):
    result = []
    total_amount = len(numbers)
    unique_amount = len(list(reduce(lambda nums, num: nums + [num] if num not in nums else nums, numbers, [])))
    once_occure_amount = len(list(reduce(lambda nums, num: nums + [num] if numbers.count(num) == 1 else nums, numbers, [])))
    max_occurance_elements = list(max(Counter(numbers).most_common(), key = lambda num: num[1]))
    print(max_occurance_elements.sort())
    result.append(total_amount)
    result.append(unique_amount)
    result.append(once_occure_amount)
    result.append(max_occurance_elements)

    return result


print(stat([1, 9, 9, 9, 9, 9, 9, 2, 2, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 7, 8]))

from functools import reduce


def stat(numbers):
    result = []
    total_amount = len(numbers)
    unique_amount = len(list(reduce(lambda nums, num: nums + [num] if num not in nums else nums, numbers, [])))
    once_occure_amount = len(list(reduce(lambda nums, num: nums + [num] if numbers.count(num) == 1 else nums, numbers, [])))
    max_occurance = max(list(reduce(lambda nums, num:  nums + [numbers.count(num)], numbers, [])))
    max_occurance_elements_all = list(filter(lambda num: numbers.count(num) == max_occurance, numbers))
    max_occurance_elements = list(reduce(lambda nums, num: nums + [num] if num not in nums else nums, max_occurance_elements_all, []))
    result.append(total_amount)
    result.append(unique_amount)
    result.append(once_occure_amount)
    result.append(max_occurance_elements)
    result.append(max_occurance)

    return result


print(stat([1, 9, 9, 9, 9, 9, 9, 2, 2, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 7, 8]))

finding_target = 7
finding_numbers = [0, 3, 5, 6, 1, 2, 4]

def is_exist_target_number_binary(target, array):
    array.sort()
    index_max = len(array) - 1
    index_min = 0
    index_half = (index_min + index_max) // 2

    while index_min <= index_max:

        if target == array[index_half]:
            return True
        elif target > array[index_half]:
            index_min = index_half + 1
        elif target < array[index_half]:
            index_max = index_half - 1

        index_half = (index_min + index_max) // 2

    return False


result = is_exist_target_number_binary(finding_target, finding_numbers)
print(result)
input = [4, 6, 2, 9, 1]


def selection_sort(array):
    max_index = len(array) - 1 

    for i in range(max_index):
        min_index = i
        for j in range(i, max_index + 1):
            if array[j] < array[min_index]:   # 현재 최솟값과 비교
                min_index = j

        array[i], array[min_index] = array[min_index], array[i]
        # print(array)

    return array


selection_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!

print("정답 = [1, 2, 4, 6, 9] / 현재 풀이 값 = ",selection_sort([4, 6, 2, 9, 1]))
print("정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ",selection_sort([3,-1,17,9]))
print("정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ",selection_sort([100,56,-3,32,44]))
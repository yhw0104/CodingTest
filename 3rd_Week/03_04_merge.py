array_a = [1, 2, 3, 5]
array_b = [4, 6, 7, 8]


def merge(array1, array2):
    aCnt = len(array1)
    bCnt = len(array2)
    index_A = 0
    index_B = 0

    array3 = []

    while index_A < aCnt and index_B < bCnt:
        if array1[index_A] <= array2[index_B]:
            # print("array1의 index_A는 ", index_A, " -> ", array1[index_A])
            # print("array2의 index_B는 ", index_B, " -> ", array2[index_B])
            array3.append(array1[index_A])
            # print("array3은 ", array3)
            index_A += 1
        elif array1[index_A] > array2[index_B]:
            # print("array1의 index_A는 ", index_A, " -> ", array1[index_A])
            # print("array2의 index_B는 ", index_B, " -> ", array2[index_B])
            array3.append(array2[index_B])
            # print("array3은 ", array3)
            index_B += 1

    if index_A == aCnt:
        for i in range(index_B, bCnt, 1):
            array3.append(array2[i])
    if index_B == bCnt:
        for i in range(index_A, aCnt, 1):
            array3.append(array1[i])

    return array3


print(merge(array_a, array_b))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!

print("정답 = [-7, -1, 5, 6, 9, 10, 11, 40] / 현재 풀이 값 = ", merge([-7, -1, 9, 40], [5, 6, 10, 11]))
print("정답 = [-1, 2, 3, 5, 10, 40, 78, 100] / 현재 풀이 값 = ", merge([-1,2,3,5,40], [10,78,100]))
print("정답 = [-1, -1, 0, 1, 6, 9, 10] / 현재 풀이 값 = ", merge([-1,-1,0], [1, 6, 9, 10]))
all_students = ["나연", "정연", "모모", "사나", "지효", "미나", "다현", "채영", "쯔위"]
present_students = ["정연", "모모", "채영", "쯔위", "사나", "나연", "미나", "다현"]


def get_absent_student(all_array, present_array):
    # 1.sort()후 반복 O(NlogN)
    # all_array.sort()
    # present_array.sort()
    # print(all_array, present_array)
    # for i in range(len(present_array)):
    #     if present_array[i] != all_array[i]:
    #         return all_array[i]
    # return all_array[len(present_array)- 1]

    # 2. 해쉬테이블 사용 O(N)
    dic = {}
    for student in all_array:
        dic[student] = True


    for present_student in present_array:
        del dic[present_student]

    for key in dic.keys():
        return key

print(get_absent_student(all_students, present_students))

print("정답 = 예지 / 현재 풀이 값 = ",get_absent_student(["류진","예지","채령","리아","유나"],["리아","류진","채령","유나"]))
print("정답 = RM / 현재 풀이 값 = ",get_absent_student(["정국","진","뷔","슈가","지민","RM"],["뷔","정국","지민","진","슈가"]))
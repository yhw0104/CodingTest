# Q.
# 1. 입력으로 소문자의 알파벳 순으로 정렬된 문자열이 입력됩니다.
# 2. 각 알파벳은 중복이 가능합니다.
# 3. 중간에 없는 알파벳이 있을 수도 있습니다.

# 입,출력 예시와 같이 입력 문자열에 나타나는 각 알파벳의 종류,갯수를 요약하여 나타내시오.

def summarize_string(input_str):
    
    alphabetList = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0, "m": 0, "n": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0}

    fullAnswer = ""
    for i in input_str:
        for alphabet in alphabetList:
            if i == alphabet:
                alphabetList[alphabet] += 1

    for alphabet in alphabetList:
        if alphabetList[alphabet] != 0:
            fullAnswer += alphabet + str(alphabetList[alphabet])
            # print(alphabetList[alphabet])

    return fullAnswer

input_str = "acccdeee"

print(summarize_string(input_str))

# def summarize_string(target_string):
#     # 이 부분을 채워보세요!
#     n = len(target_string)
#     count = 0
#     result_str = ''

#     for i in range(n - 1):
#         if target_string[i] == target_string[i + 1]:
#             count += 1
#         else:
#             result_str += target_string[i] + str(count + 1) + '/'
#             count = 0

#     result_str += target_string[n - 1] + str(count + 1)

#     return result_str


# input_str = "acccdeee"

# print(summarize_string(input_str))
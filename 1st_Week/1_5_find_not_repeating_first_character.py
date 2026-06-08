# Q. 다음과 같이 영어로 되어 있는 문자열이 있을 때, 이 문자열에서 반복되지 않는 첫번째 문자를 반환하시오. 만약 그런 문자가 없다면 _ 를 반환하시오.

def find_not_repeating_first_character(string):              

    alphabet = [0]

    for input in string:
        # list에 값 넣는 함수 append
        alphabet.append(input)
            
    for input in string:
        # list 값에서 원하는 원소의 개수 찾는 함수 count(input) 
        if alphabet.count(input) == 1:
            return input
            break

# for문 사용 시, 리스트 길이로 for문을 사용하려면 range 함수 사용 필요
# ex)
#     for input in range(len("abcdefg")):
#     ...
#     print(input)
#
#     결과값 : 0 1 2 3 4 5 6

result = find_not_repeating_first_character
print("정답 = d 현재 풀이 값 =", result("abadabac"))
print("정답 = c 현재 풀이 값 =", result("aabbcddd"))
print("정답 =_ 현재 풀이 값 =", result("aaaaaaaa"))



# def find_not_repeating_first_character(string):
#     alphabet_occurrence_array = [0] * 26

#     for char in string:
#         if not char.isalpha():
#             continue
#         arr_index = ord(char) - ord("a")
#         alphabet_occurrence_array[arr_index] += 1

#     not_repeating_character_array = []
#     for index in range(len(alphabet_occurrence_array)):
#         alphabet_occurrence = alphabet_occurrence_array[index]

#         if alphabet_occurrence == 1:
#             not_repeating_character_array.append(chr(index + ord("a")))

#     for char in string:
#         if char in not_repeating_character_array:
#             return char

#     return "_"


# result = find_not_repeating_first_character
# print("정답 = d 현재 풀이 값 =", result("abadabac"))
# print("정답 = c 현재 풀이 값 =", result("aabbcddd"))
# print("정답 =_ 현재 풀이 값 =", result("aaaaaaaa"))
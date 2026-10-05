# Q. 괄호가 바르게 짝지어졌다는 것은 '(' 문자로 열렸으면 반드시 짝지어서 ')' 문자로 닫혀야 한다는 뜻이다. 예를 들어

# ()() 또는 (())() 는 올바르다.
# )()( 또는 (()( 는 올바르지 않다.

# 이 때, '(' 또는 ')' 로만 이루어진 문자열 s가 주어졌을 때, 문자열 s가 올바른 괄호이면 True 를 반환하고 아니라면 False 를 반환하시오.

def is_correct_parenthesis(string):

    # 개수 비교 count
    open_count = 0
    close_count = 0
    for chr in string:
        if chr == "(":
            open_count += 1
        else:
            close_count += 1

    if open_count != close_count:
        return False

    array = list(string)
    while array:
        open_index = array.index("(")
        close_index = array.index(")")

        if open_index < close_index:
            array.pop(close_index)
            array.pop(open_index)
        if open_index > close_index:
            return False

    return True

    # 더 쉬운 풀이
    # count = 0
    # for ch in string:
    #     if ch == "(":
    #         count += 1
    #     else:
    #         count -= 1
    #         if count < 0:      # 닫는 괄호가 먼저 나옴
    #             return False
    # return True


print("정답 = True / 현재 풀이 값 = ", is_correct_parenthesis("(())"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis(")"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())))"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("())()"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("())()("))
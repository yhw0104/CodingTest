def find_max_occurred_alphabet(string):
    alphabet = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0, "m": 0, "n": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0}
    
    for al in string:
        if al in alphabet:
            alphabet[al] += 1

    most_used = max(alphabet, key=alphabet.get)
    
    return most_used


print("정답 = i 현재 풀이 값 =", find_max_occurred_alphabet("hello my name is dingcodingco"))
print("정답 = e 현재 풀이 값 =", find_max_occurred_alphabet("we love algorithm"))
print("정답 = b 현재 풀이 값 =", find_max_occurred_alphabet("best of best youtube"))
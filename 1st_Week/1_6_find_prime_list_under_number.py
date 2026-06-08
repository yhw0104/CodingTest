# Q. 정수를 입력 했을 때, 그 정수 이하의 소수를 모두 반환하시오. 
# 소수는 자신보다 작은 두 개의 자연수를 곱하여 만들 수 없는 1보다 큰 자연수이다.


# 내 실행 방법
def find_prime_list_under_number(number):  
    primeNum = []
    for i in range(2, number + 1):
        tf = True   #tf가 True면 소수, False면 소수가 아님        

        for i2 in range (2,i):
            if i % i2 == 0:
                tf = False

        if tf == True:
            primeNum.append(i)
        
    return primeNum

print(find_prime_list_under_number(19))


# for-else문
# 특정 반복문이 있을 때, 모두 돌았는지 안돌았는지 체크하고 싶을 때 사용
#
# for x in ["ManCity","ManCity","ManCity"]:
#    if x != "ManCity"
#        break
# else:
#    print("모두 맨시티 팬이시군요. 제가 맥주를 사겠습니다.")
#
# --> 모두 "ManCity"이기 때문에 else문 실행
#
# 그런데, 만약
# for x in ["ManCity","ManUnited","ManCity","ManCity"]:
#    if x != "ManCity"
#        break
# else:
#    print("모두 맨시티 팬이시군요. 제가 맥주를 사겠습니다.")
#
# --> 해당 리스트에는 맨유가 있기 때문에 Break문을 타게 되면서 자동으로 else문은 실행되지 않는다.

# 정리 : for-else문에서 else는 정상적으로 for문이 다 돌았을때 실행된다.


# 같이 풀어보기
def find_prime_list_under_number(number):  
    singleNum = []
    for i in range(2, number + 1):
        for i2 in range (2,i):
            if i % i2 == 0:
                break
        else:
            singleNum.append(i)
    return singleNum

print(find_prime_list_under_number(19))

#개선 1
def find_prime_list_under_number(number):  
    singleNum = []
    for i in range(2, number + 1):
        for i2 in singleNum:
            if i % i2 == 0:
                break
        else:
            singleNum.append(i)
    return singleNum

print(find_prime_list_under_number(19))
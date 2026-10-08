# dynamic programming 예시

input = 50

# memo 라는 변수에 Fibo(1)과 Fibo(2) 값을 저장해놨습니다!
memo = {
    1: 1,
    2: 1
}


def fibo_dynamic_programming(n, fibo_memo):
    # 1. memo에 n에 대한 값이 있는지 확인
    if n in fibo_memo:
        return fibo_memo[n]

    
    
    nth_fibo = fibo_dynamic_programming(n-1, fibo_memo) + fibo_dynamic_programming(n-2, fibo_memo)
    memo[n] = nth_fibo

    return nth_fibo

print(fibo_dynamic_programming(input, memo))
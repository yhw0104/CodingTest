def factorial(n):
    if n == 1:
        return 1
    answer = n * factorial(n-1)
    return answer

print(factorial(5))
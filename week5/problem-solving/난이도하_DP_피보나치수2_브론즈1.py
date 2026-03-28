# DP - 피보나치 수 2 (백준 브론즈 1)
# 문제 링크: https://www.acmicpc.net/problem/2748

n = int(input())

def fibonacci(n, memo=None):

    if memo is None:
        memo = {}

    if n <=1:
        return n
    
    if n in memo:
        return memo[n]
    
    memo[n] = fibonacci(n-1) + fibonacci(n-2)

    return memo[n]

print(fibonacci(n))
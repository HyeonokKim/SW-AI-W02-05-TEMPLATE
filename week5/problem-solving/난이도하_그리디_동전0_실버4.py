# 그리디 - 동전 0 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/11047

# n,k 입력받기 
n, k = map(int, input().split())

coins = []
result = 0 

# 반복문 실행하면서 내림차순으로 정렬
for _ in range(n):
    coins.append(int(input()))

# 반복문 실행하면서 동전 개수 구하기
for coin in reversed(coins):
    result += k//coin
    k -= coin*(k//coin)

print(result)


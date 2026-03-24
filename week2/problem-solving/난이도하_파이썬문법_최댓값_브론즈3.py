# 파이썬 문법 - 최댓값 (백준 브론즈3)
# 문제 링크: https://www.acmicpc.net/problem/2562

# numbers = [int(input()) for _ in range(9)]

numbers = []
for i in range(9):
    numbers.append(int(input()))


max_value = max(numbers)
position = numbers.index(max_value) + 1

print(max_value)
print(position)
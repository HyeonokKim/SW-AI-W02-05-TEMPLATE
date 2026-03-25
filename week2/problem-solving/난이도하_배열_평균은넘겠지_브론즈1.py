# 배열 - 평균은 넘겠지 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/4344

# 두 번째 입력값은 매 반복마다 새롭게 바뀌는 지역적인 값
# .3f = 소수점 아래 3자리 

c = int(input())

for _ in range(c):
    data = list(map(int, input().split()))
    n = data[0]
    scores = data[1:]
    
    average = sum(scores) / n

    count = 0 
    for score in scores:
        if score > average:
            count += 1

    percent = (count/n)*100
    print(f"{percent:.3f}%")


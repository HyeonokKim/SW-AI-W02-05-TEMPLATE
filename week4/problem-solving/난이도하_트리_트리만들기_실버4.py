# 트리 - 트리 만들기 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/14244

n, m = map(int, input().split())

current = 0 

# 앞부분 일직선으로 연결 
for _ in range(n-m):
    print(current, current+1)
    current += 1

# 마지막 노드에 나머지 노드를 연결
for _ in range(n-m+1, n):
    print(current,i)


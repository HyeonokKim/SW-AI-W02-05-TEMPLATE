# 분할정복 - 색종이 만들기 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/2630

# 첫 번째 방법
N = int(input())

paper = []

for _ in range(N):
    row = list(map(int,input().split()))
    paper.append(row)

white = 0 
blue = 0 

def get_paper_color(x, y, size):
    global white, blue
    first = paper[x][y]

    for i in range(x, x+size):
        for j in range(y,y+size):
            if paper [i][j] != first:
                half = size//2
                get_paper_color(x, y, half)
                get_paper_color(x, y + half, half)
                get_paper_color(x+ half, y, half)
                get_paper_color(x+half,y+half, half)
                return
            
    if first == 0:
        white += 1
    else:
        blue += 1

get_paper_color(0,0,N)
print(white)
print(blue)
        

# 두 번째 방법
def get_paper_color(x, y, size):
    first = paper[x][y]

    # 모두 같은 색인지 확인
    for i in range(x, x+size):
        for j in range(y, y+size):
            if paper[i][j] != first:
                half = size // 2

                w1, b1 = get_paper_color(x, y, half)
                w2, b2 = get_paper_color(x, y+half, half)
                w3, b3 = get_paper_color(x+half, y, half)
                w4, b4 = get_paper_color(x+ half, y+half, half)

                return (w1+w2+w3+w4, b1+b2+b3+b4)

    # 모두 같은 색이면
    if first == 0:
        return (1, 0)
    else:
        return (0, 1)
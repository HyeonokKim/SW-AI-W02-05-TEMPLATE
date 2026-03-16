# 해시 테이블 - 민균이의 비밀번호 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/9933

N = int(input()) #입력된 단어의 수
# 자료구조 정의
string = set()

# 
for _ in range(N):
    # 입력된 문자열의 공백,줄바꿈 제거 
    word = input().strip()
    # 뒤집은 문자열 출력 
    reversed_word = word [::-1]
    
    # seen 안에 있는 요소에 대해 검사
    if reversed_word in string or word == reversed_word:
        print(len(word), word[len(word)//2])
        break

    string.add(word)



# Leetcode 733
# 2D grid에서 BFS/DFS 기본 연습
# 상하좌우 탐색 패턴 익히기

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        # 시작점 색 확인 : image에서 꺼내기 
        start = image[sr][sc]

        # 시작 색과 바꿀 색이 같으면 이미지 행렬 바로 반환
        if start == color:
            return image
        
        # 재귀를 사용해 상하좌우 탐색 
        def dfs(sr, sc):
            image[sr][sc] = color

            # 상하좌우 확인
            directions = [(-1,0), (1,0), (0,-1), (0, 1)]
    
            for dr, dc in directions:
                nr = sr + dr
                nc = sc + dc

                if 0 <= nr < len(image) and 0 <= nc < len(image[0]):
                   if image[nr][nc] == start:
                       dfs(nr, nc)

        dfs(sr, sc)
        return image
        
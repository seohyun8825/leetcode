class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        row, col = len(grid), len(grid[0])
        answer = 0

        def dfs(r,c):
            if r<0 or r>= row or c<0 or c>= col or grid[r][c] == '0':
                return
            grid[r][c] = '0'
            #위 아리 왼쪽 오른쪽
            dfs(r-1, c)
            dfs(r+1, c)
            dfs(r, c-1)
            dfs(r, c+1)
        for r in range(row):
            for c in range(col):
                if grid[r][c] == '1':
                    answer+=1
                    dfs(r,c)

        return answer
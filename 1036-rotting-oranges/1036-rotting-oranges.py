class Solution(object):
    def orangesRotting(self, grid):
        queue = deque()
        n = len(grid)
        m = len(grid[0])
        time, fresh = 0, 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    queue.append((i,j))

        while queue and fresh > 0:
            for _ in range(len(queue)):
               r,c = queue.popleft()

               for dr,dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                   nr, nc = r+dr , c+dc
                   if  0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 1:
                       grid[nr][nc] = 2
                       fresh -= 1
                       queue.append((nr,nc))
            time += 1

        return time if fresh == 0 else -1
            
class Solution(object):
    def updateMatrix(self, mat):
        m = len(mat)
        n = len(mat[0])
        queue = deque()
        distance = 0
        
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i,j))
                else:
                    mat[i][j] = -1
        
        direction = [(1,0),(-1,0),(0,1),(0,-1)]

        while queue:
            size = len(queue)
            distance += 1 

            for _ in range(size):
                r,c = queue.popleft()

                for dr,dc in direction:
                    nr,nc = r+dr, c+dc
                    if 0 <= nr < m and  0 <= nc < n and mat[nr][nc] == -1:
                        mat[nr][nc] = distance
                        queue.append((nr,nc))
        return mat





            

        
        
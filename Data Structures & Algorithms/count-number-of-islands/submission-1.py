from collections import deque

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        
        islands=0
        

        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        for i in range(len(grid)):
            for j in range(len(grid[0])):

                if grid[i][j]=='1':
                    islands+=1
                    q = deque([(i,j)])
                    grid[i][j]='0'
                    while q:
                        i, j = q.popleft()
                        for di,dj in directions:
                            new_row=i+di
                            new_col=j+dj
                            if new_row<0 or new_row>=len(grid) or new_col<0 or new_col>=len(grid[0]):
                                continue
                            if grid[new_row][new_col]=='0':
                                continue
                            grid[new_row][new_col]='0'
                            q.append((new_row, new_col))
        return islands



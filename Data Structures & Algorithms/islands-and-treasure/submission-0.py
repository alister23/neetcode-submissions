class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        adjacency = {}
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != -1:
                    for a,b in [[-1,0], [1,0], [0,1], [0,-1]]:
                        if 0 <= i+a < len(grid) and 0 <= j+b < len(grid[0]):
                            if grid[i+a][j+b] != -1:
                                adjacency.setdefault((i+a,j+b),set()).add((i,j))
                    if grid[i][j] == 0:
                        adjacency.setdefault('s', set()).add((i,j))
                
        # print(adjacency)
        visited = set()
        queue = [(x,0) for x in adjacency['s']]
        # new_grid = [[0]*len(grid[0])]*len(grid)
        while queue:
            cur, dist = queue.pop(0)
            i, j = cur
            if cur not in visited:
                grid[i][j] = dist
                visited.add(cur)
                for neighbor in adjacency.setdefault(cur, []):
                    if neighbor not in visited:
                        queue.append((neighbor, dist+1))
        
        # grid = new_grid


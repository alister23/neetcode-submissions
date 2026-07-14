class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fruits = set()
        rotten = set()
        adjacency = {}
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    if grid[i][j] == 1:
                        fruits.add((i,j))
                    elif grid[i][j] == 2:
                        rotten.add((i,j))
                    adjacency[(i,j)] = set()
                    for a,b in [[0,1], [0,-1], [1,0], [-1,0]]:
                        if 0 <= i+a < len(grid) and 0 <= j+b < len(grid[0]):
                            if grid[i+a][j+b] != 0:
                                adjacency[(i,j)].add((i+a,j+b))
        queue = [(x,0) for x in rotten]
        visited = set()
        counter = 0
        while queue:
            # print(queue)
            cur, time = queue.pop(0)
            counter = time
            i,j = cur
            if cur not in visited:
                visited.add(cur)
                for neighbor in adjacency.setdefault(cur, []):
                    if neighbor not in visited and neighbor not in rotten:
                        queue.append((neighbor, time+1))
        
        # print(visited)
        # print(fruits)
        if fruits-visited:
            return -1
        return counter


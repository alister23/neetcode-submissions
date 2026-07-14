class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        adjacency = {}
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    adjacency[(i,j)] = []
                    for a,b in [[1,0], [-1,0], [0,1], [0,-1]]:
                        if 0 <= i+a < len(grid) and 0 <= j+b < len(grid[0]):
                            if grid[i+a][j+b] == 1:
                                adjacency[(i,j)].append((i+a,j+b))
        land = set(adjacency.keys())
        visited = set()
        max_area = 0
        while land:
            cur_area = 0
            queue = [land.pop()]
            while queue:
                cur_land = queue.pop(0)
                # print(cur_land)
                if cur_land not in visited:
                    cur_area += 1
                    visited.add(cur_land)
                    for neighbor in adjacency[cur_land]:
                        if neighbor not in visited:
                            queue.append(neighbor)
            # print(cur_area)
            max_area = max(max_area, cur_area)
            land -= visited
        return max_area
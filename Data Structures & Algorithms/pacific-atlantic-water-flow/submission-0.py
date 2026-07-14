class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        adjacency = {
            'p': set(),
            'a': set()
        }

        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if i == 0 or j == 0:
                    adjacency['p'].add((i,j))
                if i == len(heights)-1 or j == len(heights[0])-1:
                    adjacency['a'].add((i,j))
                adjacency[(i,j)] = set()
                for a,b in [[0,1], [0,-1], [1,0], [-1,0]]:
                    if 0 <= i+a < len(heights) and 0 <= j+b < len(heights[0]):
                        if heights[i+a][j+b] >= heights[i][j]:
                            adjacency[(i,j)].add((i+a,j+b))
        
        p_queue = list(adjacency['p'])
        p_visited = set()
        while p_queue:
            cur = p_queue.pop(0)
            if cur not in p_visited:
                p_visited.add(cur)
                for neighbor in adjacency[cur]:
                    if neighbor not in p_visited:
                        p_queue.append(neighbor)
        
        a_queue = list(adjacency['a'])
        a_visited = set()
        while a_queue:
            cur = a_queue.pop(0)
            if cur not in a_visited:
                a_visited.add(cur)
                for neighbor in adjacency[cur]:
                    if neighbor not in a_visited:
                        a_queue.append(neighbor)

        return list(p_visited.intersection(a_visited))

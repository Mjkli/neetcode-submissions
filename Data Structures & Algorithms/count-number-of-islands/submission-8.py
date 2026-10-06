from collections import deque
class Solution:
    def traverse(self, node: Tuple(int, int), grid: List):
        # check up / down / left / right
        # if neighbor in known_nodes and not in seen_nodes. recurse down
        # else ignore
        if node in self.seen_nodes:
            return
        
        self.seen_nodes.add(node)

        queue = deque()
        x = node[0]
        y = node[1]

        # check left
        if y - 1 > -1 and (x, y - 1) not in self.seen_nodes and grid[x][y - 1] == '1':
            queue.append((x, y - 1))
        # check right
        if y + 1 < len(grid[x]) and (x , y + 1) not in self.seen_nodes and grid[x][y + 1] == '1':
            queue.append((x, y + 1))

        # check down
        if x + 1 < len(grid) and (x + 1, y) not in self.seen_nodes and grid[x + 1][y] == '1':
            queue.append((x + 1, y))
        
        # check up
        if x - 1 > -1 and (x - 1, y) not in self.seen_nodes and grid[x - 1][y] == '1':
            queue.append((x - 1, y))
        

        while queue:
            self.traverse(queue.popleft(), grid)



    def numIslands(self, grid: List[List[str]]) -> int:
        self.islands = 0
        self.seen_nodes = set()
        for i, row in enumerate(grid):
            for j, col in enumerate(row):
                if grid[i][j] == '0':
                    continue
                if (i,j) in self.seen_nodes:
                    continue
                self.traverse((i,j), grid)
                self.islands += 1

        return self.islands
        
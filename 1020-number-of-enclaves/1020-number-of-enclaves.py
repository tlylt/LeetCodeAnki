class Solution:
    def bfs(self, grid, queue, visited):
        positions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        while queue:
            curr = queue.popleft()
            for pos in positions:
                row, col = curr[0] + pos[0], curr[1] + pos[1]
                if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
                    continue
                if grid[row][col] == 0 or visited[row][col]:
                    continue
                visited[row][col] = True
                queue.append([row, col])
    def numEnclaves(self, grid: List[List[int]]) -> int:
        row_len, col_len, ans = len(grid), len(grid[0]), 0
        visited = [[False for _ in range(col_len)] for _ in range(row_len)]
        queue = deque()
        for row in range(row_len):
            if grid[row][0] == 1:
                visited[row][0] = True
                queue.append((row, 0))
            if grid[row][col_len - 1] == 1:
                visited[row][col_len - 1] = True
                queue.append((row, col_len - 1))
        for col in range(1, col_len - 1):
            if grid[0][col] == 1:
                visited[0][col] = True
                queue.append((0, col))
            if grid[row_len - 1][col] == 1:
                visited[row_len - 1][col] = True
                queue.append((row_len - 1, col))
        self.bfs(grid, queue, visited)
        for row in range(row_len):
            for col in range(col_len):
                if grid[row][col] == 1 and not visited[row][col]:
                    ans += 1
        return ans
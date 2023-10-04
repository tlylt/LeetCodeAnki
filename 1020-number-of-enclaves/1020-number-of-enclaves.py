class Solution:
    def numEnclaves(self, matrix: List[List[int]]) -> int:
      WATER = 0
      LAND = 1
      VISITED_ESCAPE = 2

      NUM_ROWS = len(matrix)
      NUM_COLS = len(matrix[0])

      # runtime: O(m * n) m = rows and n = cols
      # additional space: O(m * n)
      def dfs(i, j):
        matrix[i][j] = VISITED_ESCAPE

        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        for direction in directions:
          new_i = i + direction[0]
          new_j = j + direction[1]
          # not within matrix boundaries or water or already visited and can escape
          if new_i < 0 or new_i >= NUM_ROWS or new_j < 0 or new_j >= NUM_COLS or matrix[new_i][new_j] == WATER or matrix[new_i][new_j] == VISITED_ESCAPE:
            continue

          dfs(new_i, new_j)

        return

      # mark cells as visited escape or visited cannot escape
      for i in range(NUM_ROWS):
        if matrix[i][0] == LAND:
          dfs(i, 0)
        if matrix[i][NUM_COLS - 1] == LAND:
          dfs(i, NUM_COLS - 1)

      for j in range(NUM_COLS):
        if matrix[0][j] == LAND:
          dfs(0, j)
        if matrix[NUM_ROWS - 1][j] == LAND:
          dfs(NUM_ROWS - 1, j)



      print(matrix)
      # count how many cannot escape
      count = 0
      for i in range(NUM_ROWS):
        for j in range(NUM_COLS):
          if matrix[i][j] == LAND:
            count += 1

      return count
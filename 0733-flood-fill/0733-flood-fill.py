class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        self.dfs(image, sr, sc, image[sr][sc], color)
        return image
    
    def dfs(self, image, i, j, oldColor, color):
        if i < 0 or i >= len(image) or j < 0 or j >= len(image[0]) or image[i][j] != oldColor:
            return
        image[i][j] = color
        self.dfs(image, i+1, j, oldColor, color)
        self.dfs(image, i, j+1, oldColor, color)
        self.dfs(image, i-1, j, oldColor, color)
        self.dfs(image, i, j-1, oldColor, color)
        
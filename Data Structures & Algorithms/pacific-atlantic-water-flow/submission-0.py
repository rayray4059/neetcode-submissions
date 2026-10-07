class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        def dfs(row, col, prev):
            if row < 0 or col < 0:
                return [True, False]
            if row == len(heights) or col == len(heights[0]):
                return [False, True]
            if (row, col) in visited:
                return [False, False]
            if heights[row][col] > prev:
                return [False, False]
            
            visited.add((row, col))
            up = dfs(row + 1, col, heights[row][col])
            down = dfs(row - 1, col, heights[row][col])
            left = dfs(row, col + 1, heights[row][col])
            right = dfs(row, col - 1, heights[row][col])

            pacific = up[0] + down[0] + left[0] + right[0]
            atlantic = up[1] + down[1] + left[1] + right[1]

            return [pacific > 0, atlantic > 0]

        res = []
        for r in range(len(heights)):
            for c in range(len(heights[0])):
                visited = set()
                both = dfs(r, c, 1001)
                if sum(both) > 1:
                    res.append([r, c])
                    
        return res





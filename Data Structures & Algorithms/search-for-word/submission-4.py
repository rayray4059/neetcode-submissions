class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        rows, cols = len(board), len(board[0])
        visited = set()
        
        def helper(r, c, i):
            if i == len(word):
                return True
            if r >= rows or c >= cols:
                return False
            if r < 0 or c < 0:
                return False
            if word[i] != board[r][c]:
                return False
            if (r,c) in visited:
                return False
            
            visited.add((r,c))
            res = (helper(r + 1, c, i + 1) or
                    helper(r - 1, c, i + 1) or
                    helper(r, c + 1, i + 1) or
                    helper(r, c - 1, i + 1))
            visited.remove((r,c))
            return res
        
        for r in range(rows):
            for c in range(cols):
                if helper(r,c, 0):
                    return True
        
        return False
                



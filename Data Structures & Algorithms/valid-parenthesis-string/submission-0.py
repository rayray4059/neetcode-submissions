class Solution:
    def checkValidString(self, s: str) -> bool:
        
        leftMin = 0
        leftMax = 0

        for char in s:
            if char == '(':
                leftMin += 1
                leftMax += 1
            
            if char == ')':
                leftMin -= 1
                leftMax -= 1
            
            if char == '*':
                leftMin -= 1
                leftMax += 1
            
            if leftMax < 0:
                return False
            
            if leftMin < 0:
                leftMin = 0
        
        return True if leftMin == 0 else False
           
            


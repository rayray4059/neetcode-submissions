class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] != 9:
            digits[-1] = digits[-1] + 1
            return digits
        
        for d in range(len(digits) - 1, -1, -1):
            if digits[d] + 1 > 9:
                digits[d] = 0
            else:
                digits[d] = digits[d] + 1
                return digits

            if d == 0:
                return [1] + digits 
            






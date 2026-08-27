class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid = {']':'[', '}':'{', ')':'('}
        for p in range(len(s)):
            if s[p] not in valid:
                stack.append(s[p])
            else: 
                if len(stack) > 0 and stack[-1] == valid[s[p]]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
                
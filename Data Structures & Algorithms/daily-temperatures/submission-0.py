class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        out = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            if not stack:
                stack.append((temp, i))
            
            top = stack[-1]
            if temp <= top[0]:
                stack.append((temp, i))
            else:
                while stack and temp > stack[-1][0]:
                    current = stack.pop()
                    out[current[1]] = i - current[1]
                stack.append((temp, i))
        
        if stack:
            for temp in stack:
                out[temp[1]] = 0
        
        return out




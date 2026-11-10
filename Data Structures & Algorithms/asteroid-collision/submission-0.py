class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for astr in asteroids:
            if astr > 0:
                stack.append(astr)
            else:
                alive = True
                while stack:
                    top_astr = stack[-1]
                    if top_astr < 0:
                        break
                    diff = astr + top_astr
                    if diff > 0:
                        alive = False
                        break
                    elif diff == 0:
                        stack.pop()
                        alive = False
                        break
                    else:
                        stack.pop()
                    
                if alive:
                    stack.append(astr)
            
        return stack
                    
                    
                

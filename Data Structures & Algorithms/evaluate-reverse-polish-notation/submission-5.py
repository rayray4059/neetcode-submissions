class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in "+-*/":
                stack.append(int(token))
            else:
                first = stack.pop()
                second = stack.pop()

                if token == '+':
                    stack.append((first + second))
                elif token == '-':
                    stack.append((second - first))
                elif token == '*':
                    stack.append((first * second))
                else: 
                    stack.append(int(second / first))
                
        return stack.pop()


                    

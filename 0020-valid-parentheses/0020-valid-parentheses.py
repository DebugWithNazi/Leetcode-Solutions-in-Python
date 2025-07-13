class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == "(" or char == "{" or char == "[":
                stack.append(char)
            
            else:
                if stack and char == ")" and stack[-1] == "(":
                    stack.pop()
                elif stack and char == "}" and stack[-1] == "{":
                    stack.pop()
                elif stack and char == "]" and stack[-1] == "[":
                    stack.pop()
                else:
                    stack.append(char)
        
        return len(stack) == 0
                    
                
        
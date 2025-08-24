class Solution(object):
    def dailyTemperatures(self, temperatures):
        n = len(temperatures)
        final = [0] * n 
        stack = []

        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_index = stack.pop()
                final[prev_index] = i - prev_index
            stack.append(i)
        
        return final
    
           

           
        
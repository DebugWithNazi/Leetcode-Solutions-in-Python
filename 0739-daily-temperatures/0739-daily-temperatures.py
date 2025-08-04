class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        final = [0] * n
        stack = []

        for i in range(n):

            while stack and temperatures[i] > temperatures[stack[-1]]:
                  prev_index = stack.pop()
                  final[prev_index] = i - prev_index
            stack.append(i)

        return final


        
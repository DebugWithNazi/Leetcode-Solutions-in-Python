class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        vector = values[0]
        max_score = 0

        for i in range(1,len(values)):
            max_score =max(max_score , vector + values[i] - i)
            vector = max(vector, values[i]+i)

        return max_score
            
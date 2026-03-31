class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        indices = []
        res = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            while indices != [] and temp > temperatures[indices[-1]]:
                j = indices.pop()
                res[j] = i - j
            indices.append(i)
        return res
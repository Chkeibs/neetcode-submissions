class Solution:
    def dailyTemperatures(
        self, temperatures: List[int]
    ) -> List[int]:

        n = len(temperatures)
        answer = [0] * n
        stack = []  # Stores indices

        for i, temp in enumerate(temperatures):

            while stack and temp > temperatures[stack[-1]]:
                j = stack.pop()
                answer[j] = i - j

            stack.append(i)

        return answer
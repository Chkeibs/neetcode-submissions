class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        max_len = 0

        for x in seen:
            if x - 1 not in seen:
                length = 1

                while x + length in seen:
                    length += 1

                max_len = max(max_len, length)

        return max_len
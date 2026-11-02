class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        a = sorted(nums)
        cur = 1
        ans = 1
        for i in range(len(a) - 1):
            if a[i+1] - a[i] == 1:
                cur += 1
            elif a[i+1] == a[i]:
                continue
            else:
                cur = 1
            if cur > ans:
                ans = cur
        return ans
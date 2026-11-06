class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a={}
        for i,x in enumerate(nums):
            need = target - x
            if need in a:
                return [a[need],i]
            a[x]=i

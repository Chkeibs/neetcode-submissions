class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []*len(nums)
        a=1
        pre ={}
        for i in range (len(nums)):
            a*= nums[i]
            pre[i]=a

        b=1
        suf={}
        for j in range (len(nums)-1,-1,-1):
            b*= nums[j]
            suf[j]=b
        res.append(suf[1])
        for z in range (1,len (nums)-1):
            res.append(pre[z-1]*suf[z+1])
        res.append(pre[len(nums)-2])
        return(res)
        

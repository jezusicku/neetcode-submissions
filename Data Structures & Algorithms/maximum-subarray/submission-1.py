class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = nums[0]
        curr = 0
        
        l=0
        for r in range(len(nums)):

            if curr < 0:
                curr = 0
                l = r
            curr = curr + nums[r]

            maxi = max(maxi, curr)

        return maxi
            
            
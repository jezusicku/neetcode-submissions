class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        res=[]

        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            rest = -nums[i]

            l=i+1
            r=len(nums)-1
            while l<r:
                if nums[l]+nums[r] == rest:
                    res.append([nums[i], nums[l], nums[r]])
                    l+=1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1

                elif nums[l]+nums[r] < rest:
                    l+=1

                elif nums[l]+nums[r] > rest:
                    r-=1
            
        return res


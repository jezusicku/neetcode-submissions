class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        i=0
        hashm = {}
        for i, num in enumerate(nums):
            miss=target-num
            if miss in hashm:
                return [hashm[miss], i]
            
            if num not in hashm:
                hashm[num]=i

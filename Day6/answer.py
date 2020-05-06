class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        elements = set(nums)
        
        for i in elements:
            if nums.count(i)>int(len(nums)/2):
                return i

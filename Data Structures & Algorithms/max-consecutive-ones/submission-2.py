class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        #Get the lenght of nums
        length_nums = len(nums)
        max_count = 0
        count = 0
        #Read the elements in the array 
        for i in range(length_nums):
            if nums[i] ==1: 
                count += 1
                max_count = max(max_count,count)
            else: 
                count = 0
        return max_count

class Solution:
    def missingInteger(self, nums):
        s = nums[0]
        i = 1
        while i < len(nums) and nums[i] == nums[i - 1] + 1:
            s += nums[i]
            i += 1
        while s in nums:
            s += 1
        return s
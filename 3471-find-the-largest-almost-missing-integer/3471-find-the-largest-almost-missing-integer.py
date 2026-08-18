class Solution:
    def largestInteger(self, nums, k):
        cnt = {}
        for i in range(len(nums) - k + 1):
            for x in set(nums[i:i+k]):
                cnt[x] = cnt.get(x, 0) + 1
        return max((x for x in cnt if cnt[x] == 1), default=-1)
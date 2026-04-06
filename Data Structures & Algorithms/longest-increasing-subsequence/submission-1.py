class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        res = 0
        for i in range(n-1, -1, -1):
            temp = 1
            for j in range(i+1, n):
                if nums[i] < nums[j]:
                    temp = max(temp, dp[j] + 1)
            dp[i] = temp

        return max(dp)
    
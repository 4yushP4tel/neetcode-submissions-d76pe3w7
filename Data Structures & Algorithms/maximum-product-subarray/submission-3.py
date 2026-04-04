class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        Note that the absolute value keeps increasing unless met with a zero
        then need to check on the left and right sides of the zeros.
        """
        res = curr_min = curr_max = nums[0]

        for num in nums[1:]:
            if num < 0:
                curr_min, curr_max = curr_max, curr_min
            
            temp_max = curr_max
            curr_max = max(curr_max*num, curr_min*num, num)
            curr_min = min(temp_max*num, curr_min*num, num)

            res = max(res, curr_max)
        
        return res
        
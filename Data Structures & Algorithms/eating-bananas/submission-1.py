class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        Naive approach would be to try for all values from 1->k

        A binary search could be done to try different eating ranks. 

        To calculate how much total time it would take, we would need to only check:
        T(i) = Sum(ceil(bananas/rate))
        """
        def checkTime(k: int) -> int:
            return sum((pile + k - 1) // k for pile in piles)

        piles.sort()
        n = len(piles)
        l = 1
        r = max(piles)
        while l < r:
            m = (r + l) // 2
            if checkTime(m) <= h:
                r = m
            else:
                l = m + 1
        return l
            

            

        
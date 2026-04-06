
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = defaultdict(int)
        res = 0
        l = 0
        for r in range(len(s)):
            counts[s[r]] += 1
            if k < (r - l + 1) - max(counts.values()):
                counts[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res



       
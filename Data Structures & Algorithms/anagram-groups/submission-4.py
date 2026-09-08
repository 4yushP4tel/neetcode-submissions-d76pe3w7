from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_map = defaultdict(list)

        for word in strs:
            group_map["".join(sorted(word))].append(word)
        
        return list(group_map.values())
    
        





        




                








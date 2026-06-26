from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_items = defaultdict(list)

        for item in strs:
            sorted_item = "".join(sorted(item))
            dict_items[sorted_item].append(item)
        
        return (list(dict_items.values()))


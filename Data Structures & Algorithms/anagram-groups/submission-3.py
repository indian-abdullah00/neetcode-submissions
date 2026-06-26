from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_items = defaultdict(list)
        item_key = ""

        for item in strs:
            char_nums = defaultdict(int)
            item_key = ""
            for char in item:
                char_nums[char] += 1
            for key,value in sorted(char_nums.items()):
                item_key = item_key + str(key) + str(value)
            dict_items[item_key].append(item)
        
        return list(dict_items.values())

from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_items = defaultdict(list)
        for word in strs:
            char = [0]*26
            for charctr in word:
                value = ord(charctr)
                char[value-ord('a')] +=1
            dict_items[tuple(char)].append(word)

        return list(dict_items.values())

        



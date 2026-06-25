from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        alphabets = defaultdict(int)

        for char in s:
            alphabets[char] +=1 
        
        for char in t:
            alphabets[char] -=1
        
        for value in alphabets.values():
            if value != 0:
                return False

        return True 
        
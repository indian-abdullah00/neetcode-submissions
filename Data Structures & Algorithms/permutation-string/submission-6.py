class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1)> len(s2) :
            return False
        hash_s1 = {}
        hash_s2 = {}

        l = 0
        r = 0

        for r in range(len(s1)):
            hash_s1[s1[r]] = 1 + hash_s1.get(s1[r],0)
            hash_s2[s2[r]] = 1 + hash_s2.get(s2[r],0)
        
            
        l, r = 0, len(s1) - 1



        while r < len(s2):
            if all(hash_s2.get(key, 0) == freq for key,freq in hash_s1.items()):
                return True
            r += 1
            l += 1
            if r > len(s2) -1 :
                return False
            hash_s2[s2[r]] = 1 + hash_s2.get(s2[r],0)
            hash_s2[s2[l-1]] = hash_s2.get(s2[l-1],0) - 1

            

        return False


        
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        l = 0
        r = 0
        mapping = [0]*26
        longest = 0
        duplicates = 0

        while r < len(s):
            mapping[ord(s[r])-65] += 1
            duplicates = r-l+1 - max(mapping)
            if duplicates <= k:
                longest =max(r-l+1,longest)
            # print( s[r], "r ", r, "longest ", longest, duplicates,s[l],l)              
                
            while l < len(s) and l < r and duplicates > k:
                # print("shortened")


                mapping[ord(s[l]) -65] -= 1  
                l+=1  
                duplicates = r-l+1 - max(mapping)
                
                # print( s[r], "r ", r, "longest ", longest, duplicates,s[l],l)            


            r += 1

            
            


        return longest
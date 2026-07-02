class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s = s.replace(" ","")
        j = len(s) -1
        for i in range(len(s)):
            letter = s[i].lower()
            if i == j:
                return True
            if not letter.isalnum():
                continue
            letter_2 = s[j].lower()
            while not letter_2.isalnum():
                j-=1
                letter_2 = s[j].lower()
                if i == j:
                    return True
            if letter != letter_2:
                print(letter,letter_2)
                return False
            if i >= j:
                return True
            print(i,letter,j,letter_2)

            j-=1
                

        
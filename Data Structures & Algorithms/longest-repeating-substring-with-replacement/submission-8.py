class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        l = 0
        mapping = [0] * 26
        longest = 0

        for r in range(len(s)):

            mapping[ord(s[r]) - 65] += 1

            duplicates = r - l + 1 - max(mapping)

            while duplicates > k:
                mapping[ord(s[l]) - 65] -= 1
                l += 1
                duplicates = r - l + 1 - max(mapping)

            longest = max(longest, r - l + 1)

        return longest
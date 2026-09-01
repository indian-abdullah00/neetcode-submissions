class Solution:
    def checkInclusion(self, s1, s2):
        if len(s1) > len(s2):
            return False

        count1 = {}

        # Count characters in s1
        for c in s1:
            count1[c] = count1.get(c, 0) + 1

        window = {}
        left = 0

        for right in range(len(s2)):

            # Add character to window
            window[s2[right]] = window.get(s2[right], 0) + 1

            # Keep window same size as s1
            if right - left + 1 > len(s1):
                window[s2[left]] -= 1

                if window[s2[left]] == 0:
                    del window[s2[left]]
                left += 1

            # Check if window is a permutation of s1
            if window == count1:
                return True

        return False
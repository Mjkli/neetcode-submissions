class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        max_len = 0
        window = set()
        while right <= len(s) - 1:
            if s[right] in window:
                while s[right] in window:
                    window.remove(s[left])
                    left += 1
            

            window.add(s[right])

            if len(window) > max_len:
                max_len = len(window)

            right += 1

        return max_len
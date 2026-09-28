class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp = []
        for char in s:
            if char.isalpha() or char.isnumeric():
                temp.append(char.lower())

        ptr2 = len(temp) - 1
        for i, char in enumerate(temp):
            if i == len(temp) / 2:
                break
            print(char, " ", temp[ptr2])
            if char != temp[ptr2]:
                return False
            ptr2 -= 1
        return True
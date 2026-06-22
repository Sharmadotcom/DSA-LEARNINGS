class Solution:
    def isPalindrome(self, x: int) -> bool:
        reverse = str(x)[::-1]
        if str(x) == str(reverse):
            return True
        else:
            return False
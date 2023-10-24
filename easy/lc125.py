class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss = [a.lower() for a in s if a.isalpha() or a.isalnum()]
        l, r  = 0, len(ss)-1
        while l < r:
            if ss[l] != ss[r]:
                return False
            l+=1
            r-=1
        return True





Solution().isPalindrome("A man, a plan, a canal: Panama")
Solution().isPalindrome("0P")


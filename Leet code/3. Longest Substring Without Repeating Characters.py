class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = set()
        maxL = 0
        count = 0
        firstEleofWin = 0
        for i in s:
            while i in substring:
                substring.remove(s[firstEleofWin])
                count -= 1
                firstEleofWin += 1
            substring.add(i)
            count += 1
            maxL = max(maxL, count)
        return maxL
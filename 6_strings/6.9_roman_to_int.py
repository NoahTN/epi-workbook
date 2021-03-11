# https://leetcode.com/problems/roman-to-integer
# O(n), O(1)

class Solution:
    def romanToInt(self, s: str) -> int:
        mapping = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        result = 0
        
        for i in range(len(s)):
            if i > 0 and mapping[s[i-1]] < mapping[s[i]]:
                result += mapping[s[i]] - mapping[s[i-1]]*2
            else:
                result += mapping[s[i]]
        
        return result
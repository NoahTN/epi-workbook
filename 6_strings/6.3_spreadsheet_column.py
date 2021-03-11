# https://leetcode.com/problems/excel-sheet-column-number
# O(n), O(1)

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        # Base Conversion
        for i in range(len(columnTitle)):
            value = ord(columnTitle[i]) - ord('A') + 1
            mult = 26**(len(columnTitle) - i - 1)
            result += value*mult
        return result
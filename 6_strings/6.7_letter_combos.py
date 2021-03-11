# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# O(4^n*n), O(1)

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        mapping = {'2':"abc", '3':"def", '4':"ghi", '5':"jkl", '6':"mno", '7': "pqrs", 
        '8':"tuv", '9':"wxyz"}
        
        result = ['']
        # For each digit, add and set all possible combinations to result
        for d in digits:
            result = [combo+letter for combo in result for letter in mapping[d]]
        return result
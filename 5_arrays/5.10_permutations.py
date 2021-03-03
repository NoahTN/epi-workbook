# https://leetcode.com/problems/permutations/
# O(n * n!), O(n! (Call Stack))

class Solution:
    def permute(self, nums):
        def backtrack(start, end):
            if start == end:
               # add current state of nums to result
               result.append(nums[:])
            for i in range(start, end):
               # enter path where start is swapped with nums[i]
               nums[start], nums[i] = nums[i], nums[start]
               backtrack(start+1, end)
               # restore nums to previous state
               nums[start], nums[i] = nums[i], nums[start]

        ans = []
        backtrack(0, len(nums))
        return ans
# https://leetcode.com/problems/rectangle-overlap/
# O(1), O(1)

class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        # use rightmost left
        left = max(rec1[0], rec2[0])
        # use leftmost right
        right = min(rec1[2], rec2[2])
        # use bottommost top
        top = min(rec1[3], rec2[3])
        # use topmost bottom
        bot  = max(rec1[1], rec2[1])
        # check if valid dimensions or not overlapping
        return left < right and bot < top

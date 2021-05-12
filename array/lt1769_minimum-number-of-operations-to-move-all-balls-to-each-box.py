"""
count the number of moves to move all to very left
then based on each cell, adjust the numbers

time complexity: O(n)
space complexity: O(n)
"""
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        right = 0
        balls = 0
        for idx, n in enumerate(boxes):
            if n == '1':
                right += idx
                balls += 1
        ret = [right + balls]
        tmp = (0, 0, balls)
        for i in boxes:
            left, this, right = tmp
            if i == '1':
                tmp = (left + this, 1, right - 1)
            ret.append(ret[-1] + left + this - right)
        return ret[1:]

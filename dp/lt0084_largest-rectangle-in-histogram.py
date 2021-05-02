"""
maintain a monotonous increasing stack
if new elements is smaller than stack top,
a rectangle with stack top in height and stack top to index in width could be an answer

time complexity: O(n), all elements push/poped once
space complexity: O(n) in worst case, could be a monotonous increasing list

"""
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ret = 0
        heights.append(0)
        stack = [-1]
        for i in range(len(heights)):
            while heights[stack[-1 ]] > heights[i]:
                t = stack.pop()
                h = heights[t]
                width = i - stack[-1] - 1
                ret = max(ret, width * h)
            stack.append(i)
        return ret
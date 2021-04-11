"""
use two pointers, to separate first/second/third
moving the pointer 1 position to left when needed
when second is the smallest, move first pointer to left
else move second pointer

time complexity would be O(n)
space complexity would be O(1)

"""

class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        p1 = len(arr) - 2
        p2 = len(arr) - 1
        first = 0
        for i in arr[0 :p1]:
            first = (first << 1) + i
        third = arr[-1]
        second = arr[-2]

        while p1 != 0:
            if first == third and first == second:
                return [p1 - 1, p2]
            elif first > second  and second > third and p1 < p2 - 1:
                p2 -= 1
                second = second >> 1
                third += arr[p2] << (len(arr) - p2 -1)
            elif (first > second and p1 >= p2 -1) or (first > second and third >= second):
                p1 -= 1
                first = first >> 1
                second += arr[p1] << (p2 - p1 -1)
            elif third > first and third > second:
                break
            else:
                p2 -= 1
                second = second >> 1
                third += arr[p2] << (len(arr) - p2 -1)
        return [-1, -1]


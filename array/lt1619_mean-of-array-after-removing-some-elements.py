"""
simply to sort and slince the array
time complexity: O(nlogn)
space complexity: O(n)
"""
class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        length = len(arr)
        return sum(arr[length //20 : length - length//20]) / (length - length // 10)
"""
get the pointer of each node and call the print api in reverse order

time complexity: O(n)
space complexity: O(n)
"""


# """
# This is the ImmutableListNode's API interface.
# You should not implement it, or speculate about its implementation.
# """
# class ImmutableListNode:
#     def printValue(self) -> None: # print the value of this node.
#     def getNext(self) -> 'ImmutableListNode': # return the next node.

class Solution:
    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
        l = list()
        node = head
        while node:
            l.append(node)
            node = node.getNext()
        for n in l[::-1]:
            n.printValue()
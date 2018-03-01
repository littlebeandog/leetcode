# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not (headA and headB):
            return None
        end, head_a, head_b = None, headA, headB
        while head_a is not head_b:
            print(0 if not end else end.val)
            if head_a.next is not None:
                head_a = head_a.next
            elif end is None:
                end = head_a
                head_a = headB
            elif end is not head_a:
                return None
            else:
                head_a = headB
            
            if head_b.next is not None:
                head_b = head_b.next
            elif end is None:
                end = head_b
                head_b = headA
            elif end is not head_b:
                return None
            else:
                head_b = headA
        
        return head_a

# a more consice code
# https://leetcode.com/problems/intersection-of-two-linked-lists/discuss/49798/Concise-python-code-with-comments
class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        if headA is None or headB is None:
            return None

        pa = headA # 2 pointers
        pb = headB

        while pa is not pb:
            # if either pointer hits the end, switch head and continue the second traversal, 
            # if not hit the end, just move on to next
            pa = headB if pa is None else pa.next
            pb = headA if pb is None else pb.next

        return pa
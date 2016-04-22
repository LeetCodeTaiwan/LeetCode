# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        cur1 = l1
        cur2 = l2
        if (cur1 is None and cur2 is None):
            return []
        answerRoot = ListNode(None)
        answerCur = answerRoot
        while cur1 is not None or cur2 is not None:
            if cur1 is None:
                answerCur.val = cur2.val
                cur2 = cur2.next
            elif cur2 is None:
                answerCur.val = cur1.val
                cur1 = cur1.next
            elif cur1.val < cur2.val:
                answerCur.val = cur1.val
                cur1 = cur1.next
            else:
                answerCur.val = cur2.val
                cur2 = cur2.next
            if cur1 is None and cur2 is None:
                break
            answerCur.next = ListNode(None)
            answerCur = answerCur.next
        if answerCur.val is None:
            answerCur = []

        return answerRoot

    def travelListNode(self, list):
    	while list.next != None:
    		print(str(list.val) + ' ->'),
    		list = list.next
    	print(list.val)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """


        # arr = []
        # curr = head

        # while curr:
        #     arr.append(curr)
        #     curr = curr.next
        
        # if len(arr) == 1:
        #     return arr[0].next
        # k = len(arr) - n - 1
        # if k < 0:
        #     return head.next
        # arr[k].next = arr[k].next.next

        # return head

        # k = 0 
        # curr = head
        # while curr:
        #     k+=1
        #     curr = curr.next

        # tar = k -n -1
        # if tar < 0:
        #     return head.next
        # curr = head
        # while tar > 0:
        #     curr = curr.next
        #     tar -=1

        # curr.next = curr.next.next

        # return head

        # if not head.next:
        #     return head.next

        curr1, curr2 = head,head
        while curr2 and n>0:
            curr2 = curr2.next
            n-=1

        while curr2 and curr2.next:
            curr2 = curr2.next
            curr1 = curr1.next
        
        if curr2:
            curr1.next = curr1.next.next
        else:
            return head.next

        return head


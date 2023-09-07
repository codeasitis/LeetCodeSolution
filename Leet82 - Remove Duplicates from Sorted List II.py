# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head
        else:
            dup_dict = {}
            current = head
            while current != None:
                if current.val in dup_dict:
                    dup_dict[current.val] += 1
                else:
                    dup_dict[current.val] = 1
                current = current.next
            list_values = []
            current = head
            while current != None:
                if dup_dict[current.val] > 1:
                    pass
                else:
                    list_values.append(current.val)
                current = current.next
            if list_values == []:
                return None
            else:
                node1 = ListNode(list_values[0])
                head = node1
                for entries in list_values[1:]:
                    new_node = ListNode(entries)
                    node1.next = new_node
                    node1 = new_node
                return head

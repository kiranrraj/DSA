# Date: 21/08/2025
# Question: 13
# Level: Easy
# Code: Python
# Question: Merge Sorted Linked List

# Helper Functions #
def list_to_linkedlist(lst):
    if not lst:
        return None
    
    head = ListNode(lst[0])
    current = head
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def linkedlist_to_list(head):
    lst = []
    current = head
    while current:
        lst.append(current.val)
        current = current.next
    return lst

# Main Code #
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
    dummy = ListNode()
    current = dummy
    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next

        current = current.next

    if list1:
        current.next  = list1
    elif list2:
        current.next = list2
    return dummy.next


# Convert the lists of integers to linked lists
list1_ll = list_to_linkedlist([1, 1, 3, 5, 7])
list2_ll = list_to_linkedlist([1, 2, 3, 4, 6])

# Merge the two linked lists
merged_head = mergeTwoLists(list1_ll, list2_ll)

# Convert the merged linked list back to a list for printing
print(linkedlist_to_list(merged_head))

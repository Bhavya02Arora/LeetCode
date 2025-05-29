from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first = second = head

        if not head:
            return None
        if head.next == None:
            return None
        end_reached = False
        while second and second.next and first:
            for i in range(n):
                if second is None or second.next is None:
                    end_reached = True
                    break
                second = second.next

            if end_reached or second:
                break
            first = first.next
        first.next = first.next.next

        # while second and second.next and first:
        #     first = first.next
        #     counter =0
        #     while second and second.next and counter < n:
        #         counter +=1
        #         second = second.next
        # first.next = first.next.next

        return head

    # Helper function to create a linked list from a list
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Helper function to print a linked list
def print_linked_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    print("->".join(map(str, result)))

# Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
values = [1, 2, 3, 4, 5]
head = create_linked_list(values)

# Instantiate Solution and call the method
solution = Solution()
n = 2  # Remove the 2nd node from the end
new_head = solution.removeNthFromEnd(head, n)

# Print the updated linked list
print_linked_list(new_head)

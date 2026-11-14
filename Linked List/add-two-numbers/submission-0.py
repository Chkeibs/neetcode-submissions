class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        def to_number(head):
            number = 0
            power = 1

            while head:
                number += head.val * power
                power *= 10
                head = head.next

            return number

        a = to_number(l1)
        b = to_number(l2)
        total = a + b

        dummy = ListNode(0)
        curr = dummy

        if total == 0:
            return ListNode(0)

        while total > 0:
            digit = total % 10

            curr.next = ListNode(digit)
            curr = curr.next

            total //= 10

        return dummy.next
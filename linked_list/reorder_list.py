class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reorderList(self, head):
        if not head.next: return head
        s = head.next
        n = head.next
        p = head
        while n.next:
            p = n
            n = n.next
        print(p.val)
        print(s.val)
        print()
        head.next = n
        n.next = s.next
        p.next = s
        s.next = None

        # h.next = n
        while head:
            print(head.val)
            head = head.next
        return head

if __name__ == "__main__":
    print(Solution().reorderList(ListNode(1, ListNode(2, ListNode(3, ListNode(4))))))
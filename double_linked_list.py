class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        self.previous = None

def add_node(head, value):
    new_node = ListNode(value)
    if not head:
        return new_node
    current = head
    while current.next:
        current = current.next
    current.next = new_node
    new_node.previous = current
    return head


temp = [1, 2, 3, 4]
head = None
for i in temp:
    head = add_node(head, i)

x = head
while x is not None:
    next_val = x.next.val if x.next else None
    prev_val = x.previous.val if x.previous else None
    print(f"current node: {x.val}, next node: {next_val} previous node: {prev_val}")
    x = x.next

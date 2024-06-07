class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def add_node(head, value):
    new_node = ListNode(value)
    if not head:
        return new_node
    current = head
    while current.next:
        current = current.next
    current.next = new_node
    return head

temp = [1, 2, 3, 4]
head = None
for i in temp:
    head = add_node(head, i)

x = head
while x is not None:
    next_val = x.next.val if x.next else None
    print(f"current node: {x.val}, next node: {next_val}")
    x = x.next

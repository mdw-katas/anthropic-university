"""Exploration: one interface, two representations.

reverse_via pushes every item, then pops until empty — using only the
ADT operations. Predict its output for each implementation, and predict
what ArrayStack's INTERNAL list looks like after pushing 1, 2, 3
(careful: is the top at index 0 or at the end?).

Fill the PREDICT_* constants, run this file, then:
uni grade 102/explore-02
"""

PREDICT_OUTPUTS_MATCH = None  # True/False: same result from both implementations?
PREDICT_ARRAY_INTERNAL = None  # ArrayStack internal list after push 1, push 2, push 3


class ArrayStack:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def __len__(self):
        return len(self._items)


class LinkedStack:
    def __init__(self):
        self._head = None
        self._size = 0

    def push(self, item):
        self._head = (item, self._head)
        self._size += 1

    def pop(self):
        item, self._head = self._head
        self._size -= 1
        return item

    def __len__(self):
        return self._size


def reverse_via(stack, items):
    """A client of the stack ADT: touches only push, pop, and len."""
    for item in items:
        stack.push(item)
    reversed_items = []
    while len(stack) > 0:
        reversed_items.append(stack.pop())
    return reversed_items


def array_internal_after(items):
    """Push items onto an ArrayStack and expose its representation."""
    stack = ArrayStack()
    for item in items:
        stack.push(item)
    return stack._items


if __name__ == "__main__":
    via_array = reverse_via(ArrayStack(), [1, 2, 3])
    via_linked = reverse_via(LinkedStack(), [1, 2, 3])
    print(f"reverse_via(ArrayStack(), [1, 2, 3])  = {via_array}")
    print(f"reverse_via(LinkedStack(), [1, 2, 3]) = {via_linked}")
    print(f"outputs match: {via_array == via_linked}")
    print(f"ArrayStack internal list after pushes: {array_internal_after([1, 2, 3])}")

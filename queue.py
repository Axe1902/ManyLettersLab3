class Queue:
    def __init__(self):
        self._head = None
        self._tail = None
        self.len = 0

    def add(self, data):
        node = Node(data)
        if self._head is None:
            self._head = node
            self._tail = node
        else:
            self._tail.next = node
            self._tail = node
        self.len += 1

    def pop(self):
        to_ret = self._head
        self._head = self._head.next
        self.len -= 1
        return to_ret.data


class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

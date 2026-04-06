from collections import defaultdict

class Node:

    def __init__(self, key: int, value:int):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.cache = {}
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        node = self.cache.get(key, None)
        if node:
            self._moveNodeToFront(node)
            return node.value
        else:
            return -1
        
    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key, None)
        if node:
            node.value = value
            self._moveNodeToFront(node)
        else:
            node = Node(key, value)
            self._addNodeToFront(node)

            if self.size > self.capacity:
                self._removeLastNode()

        self.cache[key] = node

    
    def _removeNode(self, node: Node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1
    
    def _addNodeToFront(self, node: Node) -> None:
        temp = self.head.next
        temp.prev = node
        node.next = temp
        self.head.next = node
        node.prev = self.head
        self.size += 1
    
    def _moveNodeToFront(self, node: Node) -> None:
        self._removeNode(node)
        self._addNodeToFront(node)
    
    def _removeLastNode(self) -> None:
        temp = self.tail.prev
        temp.prev.next = self.tail
        self.tail.prev = temp.prev
        del self.cache[temp.key]
        self.size -= 1



        

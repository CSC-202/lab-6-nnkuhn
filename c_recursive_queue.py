# Recursive Queue
# Author: Nathan Kuhn

class Node:
    value: any
    next: any

    def __init__(self, value, next):
        self.value = value
        self.next = next


class Queue:
    first: Node
    last: Node

    def __init__(self):
        self.first = None
        self.last = None

    def __len__(self):
        n: int = 0
        current = self.first
        while current != None:
            n += 1
            current = current.next
        return n

    def toPythonList(self):
        result: list = []
        current = self.first
        while current != None:
            result.append(current.value)
            current = current.next
        return result


def initialize() -> Queue:
    return Queue()


def isEmpty(data: Queue) -> bool:
    return data.first == None


def enqueue(data: Queue, value: int) -> Queue:
    if data.last is None:
        data.last = Node(value, None)
        data.first = data.last
        return data
    else:
        data.last.next = Node(value,None)
        data.last = data.last.next
        return data


def dequeue(data: Queue) -> tuple[Node, Queue]:
    node = data.first
    data.first = data.first.next
    return [node, data]


def peek(data: Queue) -> Node:
    return data.first


def clear(data: Queue) -> Queue:
    data = Queue()
    return data


'''nums = initialize()
print(Queue.toPythonList(nums))
print()

nums = enqueue(nums,1)
print(Queue.toPythonList(nums))
print()

nums = enqueue(nums,2)
print(Queue.toPythonList(nums))
print()

nums = dequeue(nums)
print(nums[0].value, Queue.toPythonList(nums[1]))
nums = nums[1]
print()

print(peek(nums).value)'''
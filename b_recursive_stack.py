# Recursive Stack
# Author: Nathan Kuhn

class Node:
    value: any
    next: any

    def __init__(self, value, next):
        self.value = value
        self.next = next


class Stack:
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


def initialize() -> Stack:
    return Stack()


def isEmpty(data: Stack) -> bool:
    return data.first == None


def push(data: Stack, value: int) -> Stack:
    data.first = Node(value, data.first)
    return data


def pop(data: Stack) -> tuple[Node, Stack]:
    node = data.first
    data.first = data.first.next
    return [node, data]


def peek(data: Stack) -> Node:
    return data.first


def clear(data: Stack) -> Stack:
    data = Stack()
    return data


'''nums = initialize()
print(Stack.toPythonList(nums))
print()

nums = push(nums,1)
print(Stack.toPythonList(nums))
print()

nums = push(nums,2)
print(Stack.toPythonList(nums))
print()

nums = pop(nums)
print(nums[0].value, Stack.toPythonList(nums[1]))
nums = nums[1]
print()

print(peek(nums).value)'''
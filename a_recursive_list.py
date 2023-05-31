# Recursive List
# Author: Nathan Kuhn

class Node:
    value: any
    next: any

    def __init__(self, value, next):
        self.value = value
        self.next = next


class List:
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


def initialize() -> List:
    lst = List()
    lst.first = Node(None,None)
    lst.last = lst.first
    return lst


def isEmpty(data: List) -> bool:
    return data.first == None


def addToFront(data: List, value: int) -> List:
    if isEmpty(data) == True:
        data.first = Node(value, data.last)
        return data
    else:
        new_node = Node(value, data.first)
        data.first = new_node
        return data

def addAtIndex(data: List, index: int, value: int) -> List:
    new_node = Node(value, next)
    def helper(first: Node, index: int, value: int, count):
        if count == index - 1:
            new_node.next = first.next
            first.next = new_node
            return data
        elif first != None:
            return helper(first.next, index, value, count + 1)
    if isEmpty(data) == True:
        return None
    elif index < 0 or index >= len(data) + 1:
        raise IndexError('oops')
    elif index == 0:
        return addToFront(data, value)
    else:
        return helper(data.first, index, value, 0)
    

def removeAtIndex(data: List, index: int) -> tuple[Node, List]:
    def helper(first: Node, index: int, count):
        if count == index - 1:
            node = first.next
            first.next = node.next
            return [node, data]
        elif first != None:
             return helper(first.next, index, count + 1)
    if isEmpty(data) == True:
        return None
    elif index < 0 or index >= len(data):
        raise IndexError('oops')
    elif index == 0:
        # node = data.first
        # data.first = node.next
        return [None, data]
    else:
        return helper(data.first, index, 0)


def addToBack(data: List, value: int) -> List:
    if isEmpty(data) == True:
        data.first = Node(value, None)
        return data
    else:
        return addAtIndex(data, len(data), value)


def getElementAtIndex(data: List, index: int) -> Node:
    def helper(first: Node, index: int, count):  
        if count == index:
            return Node(first.value,None)
        elif first != None:
            return helper(first.next, index, count + 1)
    if data.first.next == None:
        return Node(data.first.value,None)
    elif isEmpty(data) == True:
        return None
    elif index < 0 or index >= len(data):
        raise IndexError('oops')
    elif data.first != None:
        return helper(data.first, index, 0)

def clear(data: List) -> List:
    data = List()
    return data


'''nums = List()
print(List.toPythonList(nums))

print(isEmpty(nums))

nums = addToFront(nums, 2)
print(List.toPythonList(nums))

nums = addToBack(nums, 5)
print(List.toPythonList(nums))

nums = addToFront(nums, 1)
print(nums.toPythonList())

nums = addAtIndex(nums, 2, 3)
print(nums.toPythonList())

nums = addAtIndex(nums, 3, 4)
print(List.toPythonList(nums))

nums = addAtIndex(nums, 5, 6)
print(List.toPythonList(nums))

print(getElementAtIndex(nums,3).value)
print(List.toPythonList(nums))

node, nums = removeAtIndex(nums,2)
print(node.value)
print(List.toPythonList(nums))'''
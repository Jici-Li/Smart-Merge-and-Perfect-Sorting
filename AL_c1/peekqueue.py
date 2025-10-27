# File:    peekqueue.py
# Author:  John Longley
# Date:    October 2022

# Linked list implementation of queues allowing peeking
# Adapted from Franz Miltz's LL_Queue

class PeekQueue:
    def __init__(self):
        self.tail = PeekQueueCell()
        self.head = self.tail

    def peek(self):
        if self.head == None:
            return None
        else:
            return self.head.value

    def push(self, value):
        self.tail.value = value
        self.tail.next = PeekQueueCell()
        self.tail = self.tail.next

    def pop(self):
        if self.head == None:
            return None
        else:
            value = self.head.value
            self.head = self.head.next
            return value

class PeekQueueCell:
    def __init__(self):
        self.next = None
        self.value = None

# For testing:

def queueToList(Q):
    L = []
    while Q.peek() != None:
        L.append(Q.pop())
    return L

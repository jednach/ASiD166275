class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, value):
        self.head = Node(value, self.head)

    def append(self, value):
        if self.head is None:
            self.head = Node(value, self.head)
        else:
            i = self.head
            while i.next:
                i = i.next
            i.next = Node(value, None)

    def node(self, index):
        len = 0
        i = self.head
        while i:
            len += 1
            i = i.next

        if self.head is None or len - 1 < index:
            print("lista jest pusta lub krotsza od podanej wartosci")
            return

        j = self.head
        k = 0
        while j:
            if k == index:
                return j
            k += 1
            j = j.next

    def insert(self, value, wezel):
        if self.head is None:
            print("lista jest pusta lub krotsza od podanej wartosci")
            return

        wezel.next = Node(value, wezel.next)

    def __len__(self):
        len = 0
        i = self.head
        while i:
            len += 1
            i = i.next
        return len

    def pop(self):
        if self.head is None:
            print("lista jest pusta brak elementow do usuniecia")
            return
        temp = self.head.value
        self.head = self.head.next
        return temp

    def remove_last(self):
        if self.head is None:
            print("lista jest pusta brak elementow do usuniecia")
            return

        len = 0
        i = self.head
        while i:
            len += 1
            i = i.next

        j = self.head
        if len == 1:
            a = j.value
            self.head = None
            return a

        k = 0
        while j:
            if k == len - 2:
                a = j.next.value
                j.next = None
                break
            k += 1
            j = j.next
        return a

    def remove(self, wezel):

        if self.head is None:
            print("lista jest pusta lub zbyt krotka by mozliwe bylo usuniecie danego wezla")
            return
        wezel.next = wezel.next.next

    def __str__(self):
        if self.head is None:
            return "lista jest pusta"

        i = self.head
        llstr = ''

        while i:
            if i.next is None:
                llstr += str(i.value)
            else:
                llstr += str(i.value) + ' -> '
            i = i.next

        return llstr


class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):
        self.head = Node(value, self.head)

    def pop(self):
        if self.head is None:
            print("lista jest pusta brak elementow do usuniecia")
            return
        temp = self.head.value
        self.head = self.head.next
        return temp

    def __len__(self):
        len = 0
        i = self.head
        while i:
            len += 1
            i = i.next
        return len

    def __str__(self):
        if self.head is None:
            return "lista jest pusta"

        i = self.head
        llstr = ''

        while i:
            if i.next is None:
                llstr += str(i.value)
            else:
                llstr += str(i.value) + ' -> '
            i = i.next

        return llstr


class Queue:
    def __init__(self):
        self.head = None

    def peek(self):
        return self.head.value

    def enqueue(self, value):
        self.head = Node(value, self.head)

    def dequeue(self):
        if self.head is None:
            print("lista jest pusta brak elementow do usuniecia")
            return

        len = 0
        i = self.head
        while i:
            len += 1
            i = i.next

        j = self.head
        if len == 1:
            a = j.value
            self.head = None
            return a

        k = 0
        while j:
            if k == len - 2:
                a = j.next.value
                j.next = None
                break
            k += 1
            j = j.next
        return a

    def __len__(self):
        len = 0
        i = self.head
        while i:
            len += 1
            i = i.next
        return len

    def __str__(self):
        if self.head is None:
            return "lista jest pusta"

        i = self.head
        llstr = ''

        while i:
            if i.next is None:
                llstr += str(i.value)
            else:
                llstr += str(i.value) + ', '
            i = i.next

        return llstr


list_ = LinkedList()

assert list_.head == None
list_.push(1)
list_.push(0)
assert str(list_) == '0 -> 1'

list_.append(9)
list_.append(10)

assert str(list_) == '0 -> 1 -> 9 -> 10'

middle_node = list_.node(1)
list_.insert(5, middle_node)

assert str(list_) == '0 -> 1 -> 5 -> 9 -> 10'

first_element = list_.node(0)
returned_first_element = list_.pop()

assert first_element.value == returned_first_element

last_element = list_.node(3)
returned_last_element = list_.remove_last()

assert last_element.value == returned_last_element
assert str(list_) == '1 -> 5 -> 9'

second_node = list_.node(1)
list_.remove(second_node)

assert str(list_) == '1 -> 5'
stack = Stack()

assert len(stack) == 0

stack.push(3)
stack.push(10)
stack.push(1)

assert len(stack) == 3

top_value = stack.pop()
assert top_value == 1

assert len(stack) == 2

queue = Queue()

assert len(queue) == 0

queue.enqueue('klient1')
queue.enqueue('klient2')
queue.enqueue('klient3')
print(str(queue))
assert str(queue) == 'klient1, klient2, klient3'

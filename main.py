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
            if (k == index):
                return j.value
            k += 1
            j = j.next

    def insert(self, value, index):
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
                j.next = Node(value, j.next)
                break
            k += 1
            j = j.next

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
        k = 0
        j = self.head
        while j:
            if k == len - 2:
                a = j.next.value
                j.next = None
                break
            k += 1
            j = j.next
        return a

    def remove(self, index):
        len = 0
        i = self.head
        while i:
            len += 1
            i = i.next

        if self.head is None or len - 2 < index:
            print("lista jest pusta lub zbyt krotka by mozliwe bylo usuniecie danego wezla")
            return

        j = self.head
        k = 0
        while j:
            if k == index:
                a = j.next.value
                j.next = j.next.next
                return a
            k += 1
            j = j.next

    def len(self):
        leng = 0
        i = self.head
        while i:
            leng += 1
            i = i.next
        return leng

    def print(self):
        if self.head is None:
            print("lista jest pusta")
            return

        i = self.head
        llstr = ''

        while i:
            if i.next is None:
                llstr += str(i.value)
            else:
                llstr += str(i.value) + ' -> '
            i = i.next

        print(llstr)


ll = LinkedList()

ll.push(1)
ll.append(3)
ll.push(0)
#print(ll.node(2))
ll.insert(2,1)
print(ll.len())
ll.print()
#print(ll.pop())
#print(ll.remove_last())
print(ll.remove(1))
print(ll.len())
ll.print()


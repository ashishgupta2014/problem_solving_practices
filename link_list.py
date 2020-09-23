class Node:
    def __init__(self, data=None):
        self.data = data
        self.link = None


class SingleLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        if self.head:
            self.last().link = Node(data)
        else:
            self.head = Node(data)

    def last(self):
        val = self.head
        while val is not None:
            node = val
            val = val.link
        return node

    def len(self):
        count = 0
        val = self.head
        while val is not None:
            count += 1
            val = val.link
        return count

    def postionalInsert(self, position, data):
        if self.head:
            if position > 0:
                val = self.head
                while val is not None:
                    position -= 1
                    if position == 0:
                        current_node = val
                        next_node = val.link
                        current_node.link = Node(data)
                        current_node.link.link = next_node
                    val = val.link
            elif position == 0:
                current_node = self.head
                self.head = Node(data)
                self.head.link = current_node
        else:
            self.insert(data)

    def list(self):
        val = self.head
        while val is not None:
            print(val.data)
            val = val.link


if __name__:
    list1 = SingleLinkedList()
    list1.insert("Mon")
    list1.insert("Tue")
    list1.insert("Thr")
    list1.postionalInsert(0, "Sun")
    list1.postionalInsert(3, "Wed")
    list1.list()
    print(list1.len())

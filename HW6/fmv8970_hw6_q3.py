from DoublyLinkedList import DoublyLinkedList
class CompactString:
    def __init__(self, orig_str):
        self.dll = DoublyLinkedList()
        char = ''
        count = 0
        node = self.dll.header.next
        for x in orig_str:
            if x.isalpha():
                if char == '':
                    char = x
                    count = 1
                elif x is not char:
                    self.dll.add_last((char, count))
                    char = x
                    count = 1
                else:
                    count += 1
        if char != '':
            self.dll.add_last((char, count))

    def __add__(self, other):
        res_cs = CompactString("")
        node = self.dll.header.next
        while node.data is not None:
            res_cs.dll.add_last(node.data)
            node = node.next
        node = other.data.header.next
        while node.data is not None:
            res_cs.dll.add_last(node.data)
            node = node.next
        return res_cs

    def __lt__(self, other):
        if self.dll.is_empty() and other.data.is_empty():
            return True
        if self.dll.is_empty():
            return True
        if other.data.is_empty():
            return False
        node_s = self.dll.header.next
        node_o = other.data.header.next
        if node_s.data[0] > node_o.data[0]:         # if self first char is greater
            return False
        elif node_o.data[0] > node_s.data[0]:       # if other first char is greater
            return True
        else:
            if node_o.data[1] > node_s.data[1]:      # if other set of letters is longer
                if node_s.next.data is None:
                    return True
                else:
                    return node_s.next.data[0] < node_o.data[0]
            else:                               # if self set of letters is longer
                if node_o.next.data is None:
                    return False
                else:
                    return node_s.data[0] < node_o.next.data[0]


    def __le__(self, other):
        if self.dll.is_empty() and other.data.is_empty():
            return True
        if self.dll.is_empty():
            return True
        if other.data.is_empty():
            return False
        if self < other:
            return True
        else: #self == other
            snode = self.dll.header.next
            onode = other.data.header.next
            while snode is not None and onode is not None:
                if snode.data[0] != onode.data[0]:
                    return False
                if not(snode.next.data is None and onode.next.data is None):
                    snode = snode.next
                    onode = onode.next
            return True

    def __gt__(self, other):
        return not self <= other

    def __ge__(self, other):
        return not self < other

    def __repr__(self):
        res = ""
        for x in self.dll:
            res += x[0] * x[1]
        return res

s1 = CompactString('aaaaabbbaaac')
s2 = CompactString('aaaaaaacccaaaa')
s3 = s1 + s2  # aaaaabbbaaacaaaaaaacccaaaa
s4 = s2 + s1  # aaaaaaacccaaaaaaaaabbbaaac
print(s1)
print(s2)
print(s3)
print(s4)
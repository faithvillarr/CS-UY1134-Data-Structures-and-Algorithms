from DoublyLinkedList import DoublyLinkedList


class Integer:
    def __init__(self, num_str):
        self.dll = DoublyLinkedList()
        for i in num_str:
            self.dll.add_last(int(i))
        while self.dll.header.next.data == 0 and len(self.dll) > 1:
            self.dll.delete_first()



    
    def __add__(self, other):
        new_num = Integer("")
        node_s = self.dll.trailer.prev
        node_o = other.dll.trailer.prev
        carried = 0
        while not(node_s.data is None or node_o.data is None):
            added = node_s.data + node_o.data + carried
            new_num.dll.add_first(added % 10)
            carried = added // 10
            node_s = node_s.prev
            node_o = node_o.prev
        # now we have some carried and placed all known values in a list
        # either node_o is None or node_s is None or both are None
        if node_o.data is not None:
            extra = node_o
        else:
            extra = node_s
        while extra.data is not None:
            new_num.dll.add_first((extra.data + carried) % 10)
            carried = (extra.data + carried) // 10
            extra = extra.prev
        if carried != 0:
            new_num.dll.add_first(carried)
        return new_num

    def __repr__(self):
        res = ""
        node = self.dll.header.next
        for i in range(len(self.dll)):
            res += str(node.data)
            node = node.next
        return res

    def __mul__(self, other):
        res_num = Integer("")
        node_s = self.dll.trailer.prev
        for i in range(len(self.dll)):
            node_o = other.dll.trailer.prev
            carried = 0
            temp = Integer("")
            for j in range(len(other.dll)):
                added = node_s.data * node_o.data + carried
                temp.dll.add_first(added % 10)
                carried = added // 10
                node_o = node_o.prev
            if carried != 0:
                temp.dll.add_first(carried)
            for j in range(i):
                temp.dll.add_last(0)
            res_num = res_num + temp
            node_s = node_s.prev
        while res_num.dll.header.next.data == 0 and len(res_num.dll) > 1:
            res_num.dll.delete_first()
        return res_num
def main():
    a = Integer("8432926478032658043678")
    b = Integer("0783326743657285678432")
    print(a + b)
    print(8432926478032658043678 + 783326743657285678432)

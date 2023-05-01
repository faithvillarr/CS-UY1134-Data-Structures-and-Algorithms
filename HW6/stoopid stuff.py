def stOOped_me(self, other):
    node_s = self.data.header.next
    node_o = other.data.header.next
    if node_o.data is None or node_s.data is None:
        raise Exception("CompactString is empty")
    if node_s.data[0] > node_o.data[0]:  # if self first char is greater
        return False
    elif node_o.data[0] > node_s.data[0]:  # if other first char is greater
        return True
    else:
        if node_o.data[1] == node_s.data[1]:  # if the set of letters is equal
            while node_o.data[0] == node_s.data[0] and node_o.data[1] == node_s.data[
                1] and node_o.next.data is not None and node_s.next.data is not None:
                node_o = node_o.next
                node_s = node_s.next
            # when loop breaks, either (1) different character or (2) different length of same character of
            #                           or (3) diff length of diff chars or (4) one is empty
            #                           or (5) both are empty
            if (
                    node_o.next.data is None and node_s.next.data is None) or node_s.next.data is None:  # if both are empty or self is empty
                return True
            elif node_o.next.data is None:
                return False
            elif node_s.data[0] != node_o.data[0]:  # if diff length and diff char or diff char only
                return node_s.data[0] < node_o.data[0]
            elif node_s.data[1] != node_o.data[1]:  # if diff length only
                return node_s.data[1] < node_o.data[1]

        elif node_o.data[1] > node_s.data[1]:  # if other set of letters is longer
            if node_s.next.data is None:
                return True
            else:
                return node_s.next.data[0] <= node_o.data[0]
        else:  # if self set of letters is longer
            if node_o.next.data is None:
                return False
            else:
                return node_s.data[0] <= node_o.next.data[0]

            s1 = CompactString('aaaaabbbaaac')
            s2 = CompactString('aaaaaaacccaaaa')
            s1 + s2  # aaaaabbbaaacaaaaaaacccaaaa
            s2 + s1  # aaaaaaacccaaaaaaaaabbbaaac
            print(s1 < s2)  # False
            print(s2 < s1)  # True
            print(s1 <= s2)  # False
            print(s2 <= s1)  # True
            print(s1 > s2)  # True
            print(s2 > s1)  # False
            print(s1 >= s2)  # True
            print(s2 >= s1)  # False
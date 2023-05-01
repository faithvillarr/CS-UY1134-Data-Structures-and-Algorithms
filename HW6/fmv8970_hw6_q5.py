from DoublyLinkedList import DoublyLinkedList


def merge_linked_lists(srt_lnk_lst1, srt_lnk_lst2):
    res_lst = DoublyLinkedList()
    #either...
    # (1) they are both empty
    # (2) one is empty
    # (3) one is longer
    # (4) they are the same length(?)

    #(1)
    if srt_lnk_lst1.is_empty() and srt_lnk_lst2.is_empty(): # both lists are empty
        return res_lst
    #(2)
    elif srt_lnk_lst1.is_empty():
        return srt_lnk_lst2
    elif srt_lnk_lst2.is_empty():
        return srt_lnk_lst1

    # (3) & (4)
    def merge_sublists(sub_list_1, node1, sub_list_2, node2):
        if node1 is sub_list_1.trailer or node2 is sub_list_2.trailer: #one is longer or they could be same
            if node1 is sub_list_1.trailer and node2 is sub_list_2.trailer:
                return res_lst
            elif node1 is sub_list_1.trailer:
                while node2 is not sub_list_2.trailer:
                    res_lst.add_last(node2.data)
                    node2 = node2.next
            else: # node2 is sub_list_1.trailer
                while node1 is not sub_list_1.trailer:
                    res_lst.add_last(node1.data)
                    node1 = node1.next
        else:
            if node1.data < node2.data:
                res_lst.add_last(node1.data)
                merge_sublists(sub_list_1, node1.next, sub_list_2, node2)
            else:
                res_lst.add_last(node2.data)
                merge_sublists(sub_list_1, node1, sub_list_2, node2.next)
    merge_sublists(srt_lnk_lst1, srt_lnk_lst1.header.next, srt_lnk_lst2, srt_lnk_lst2.header.next)
    return res_lst



def main():
    x = DoublyLinkedList()
    for i in range(3,5):
        x.add_last(i)
    y = DoublyLinkedList()
    for i in range(10,15):
        y.add_last(i)
    z = merge_linked_lists(x, y)
    print(z)

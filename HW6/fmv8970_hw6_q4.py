from DoublyLinkedList import DoublyLinkedList

def copy_linked_list(lnk_lst):
    res_lst = DoublyLinkedList()
    for x in lnk_lst:
        res_lst.add_last(x)
    return res_lst

def deep_copy_linked_list(lnk_lst):
    res_lst = DoublyLinkedList()
    for x in lnk_lst:
        if isinstance(x, int):
            res_lst.add_last(x)
        else:
            res_lst.add_first(deep_copy_linked_list(x))
    return res_lst
from BinarySearchTreeMap import BinarySearchTreeMap
def restore_bst(prefix_lst):
    tree = BinarySearchTreeMap()
    def helper(tree, prefix_list, start, end):
        if start == end:
            if start < len(prefix_lst):
                tree.insert(prefix_list[start], None)
            return
        else:
            tree.insert(prefix_list[start], None)
            a = start+ 1
            pivot = 0
            while a < end and pivot ==0:
                if(prefix_list[start]>=prefix_list[a]):
                    a += 1
                else:
                    pivot = a

            if pivot != start:
                if pivot != 0:
                    helper(tree,prefix_list, start+1, pivot-1)
                else:
                    helper(tree, prefix_list, start+1, end)
            if pivot != 0:
                helper(tree, prefix_list, pivot, end)
            return
    helper(tree, prefix_lst, 0, len(prefix_lst))
    return tree

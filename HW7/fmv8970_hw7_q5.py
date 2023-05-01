#operator will be a root
#node is either a int or an op

#need to keep track of a cursor so tuple
from LinkedBinaryTree import LinkedBinaryTree

def create_expression_tree(prefix_exp_str):
    lst = prefix_exp_str.split()
    if len(lst) == 0:
        return LinkedBinaryTree(None)
    #treat it like a pointer, return tuple that has curr node and
    def sub_expression_tree(ind):
        if lst[ind].isdigit():
            return (ind + 1, LinkedBinaryTree.Node(int(lst[ind])))
        #the lst[ind] is an operator
        left = sub_expression_tree(ind+1) #returns a tuple with an ind and child
        right = sub_expression_tree(left[0])  # so it keeps a more current counter
        parent_node = LinkedBinaryTree.Node(lst[ind], left[1], right[1])
        return (right[0], parent_node)
    return LinkedBinaryTree(sub_expression_tree(0)[1])


def prefix_to_postfix(prefix_exp_str):
    return " ".join(str(i.data) for i in (create_expression_tree(prefix_exp_str)).postorder())


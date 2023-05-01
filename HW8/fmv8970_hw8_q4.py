import math
from BinarySearchTreeMap import BinarySearchTreeMap

def find_min_abs_difference(bst):
    if bst.is_empty():
        raise Exception("no min absolute difference on an empty tree")
    if not(bst.root.left or bst.root.right):
        raise Exception("no min absolute difference on a tree with only one node")
    def sub_difference(node):
        if not(node.left or node.right):
            return (node.item.key, node.item.key, None)
        else:
            if (not node.left) and node.right:
                right = sub_difference(node.right)
                min = node.item.key
                max = right[1]
                cont = (right[0] - node.item.key, right[2])
            elif (not node.right) and node.left:
                left = sub_difference(node.left)
                min = left[0]
                max = node.item.key
                cont = (node.item.key - left[1], left[2])
            else:
                right = sub_difference(node.right)
                left = sub_difference(node.left)
                min = left[0]
                max = right[1]
                cont = (node.item.key - left[1], right[0]-node.item.key, left)
            res = min(i for i in cont if i is not None)
            return min, max, res
    return sub_difference(bst.root)[2]



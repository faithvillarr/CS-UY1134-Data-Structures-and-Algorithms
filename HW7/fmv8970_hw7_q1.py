from LinkedBinaryTree import LinkedBinaryTree
def min_and_max(bin_tree): # returns tuple w min and max of tree
    if not bin_tree.root:
        raise Exception("min and max are undefined")
    def subtree_min_and_max(root):
        #if leaf, return data in tuple
        if not(root.left or root.right):
            return (root.data, root.data)
        else:
            res = (root.data, root.data)
            if root.left:
                left = subtree_min_and_max(root.left)
                if left[0]<res[0]:
                    res = (left[0], res[1])
                if left[1] > res[1]:
                    res = (res[0], left[1])
            if root.right:
                right = subtree_min_and_max(root.right)
                if right[0]<res[0]:
                    res = (right[0], res[1])
                if right[1] > res[1]:
                    res = (res[0], right[1])
            return res
    return subtree_min_and_max(bin_tree.root)


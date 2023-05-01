def is_height_balanced(bin_tree):
    if not bin_tree.root:
        raise Exception("tree is empty so we cant test this dumb dumb")
    def is_subtree_height_balanced(root):
        if not root:
            return (0, True) #(height, if still true)
        else:
            left = is_subtree_height_balanced(root.left)
            right = is_subtree_height_balanced(root.right)
            temp1 = (abs(left[0]-right[0])<=1) and right[1] and left[1]
            return (max(left[0], right[0]) + 1, temp1)
    return is_subtree_height_balanced(bin_tree.root)[1]




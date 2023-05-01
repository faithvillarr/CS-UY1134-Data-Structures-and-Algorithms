from BinarySearchTreeMap import BinarySearchTreeMap
tree = BinarySearchTreeMap(None)

tree[1] = None
tree[4] = None
tree[6] = None
tree[7] = None
tree[17] = None
tree[25] = None
tree[9] = None
tree[20] = None


for i in tree.inorder():

    pass #print(i.item.key, end=' ')

#print(find_min_abs_difference(tree))

lst = [1,-1,-1,-1,-1,-5,3,3]
a =1
while lst[0]> lst[a]:
    a +=1
print(lst[a])

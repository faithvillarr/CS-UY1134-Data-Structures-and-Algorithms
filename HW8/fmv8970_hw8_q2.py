from BinarySearchTreeMap import BinarySearchTreeMap
def create_chain_bst(n):
    bst = BinarySearchTreeMap()
    for i in range(1, n+1):
        bst.insert(i,None)
    return bst

def create_complete_bst(n): #7 middle would be 4
    bst = BinarySearchTreeMap()
    add_items(bst,1,n)
    return bst

def add_items(bst, low, high):
    if low >= high:
        bst.insert(low, None)
    else:
        mid = (low  + high)//2
        bst.insert(mid, None)
        add_items(bst, low, mid-1)
        add_items(bst, mid+1, high)

def list_min(lst, low, high):
    if len(lst) == 0 or not isinstance(lst[low], int):
        return None
    elif low == high:
        return lst[low]
    else:
        if lst[low]>lst[high]:
            return list_min(lst,low+1,high)
        else:
            return list_min(lst, low, high-1)



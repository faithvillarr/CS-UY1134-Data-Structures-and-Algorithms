def split_by_sign(lst,low,high):
    if len(lst) == 0 or len(lst) ==1:
        return lst
    elif low == high:
        return lst
    else:
        if lst[low]>0:
            lst.append(lst.pop(low))
            return split_by_sign(lst,low,high-1)
        else:
            return split_by_sign(lst, low+1,high)

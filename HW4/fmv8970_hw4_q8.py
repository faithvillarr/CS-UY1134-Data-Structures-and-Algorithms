def flat_list(nested_lst, low, high):
    if len(nested_lst) == 0:
        return []
    else:
        res_lst = []
        while not (low > high):
            if (isinstance(nested_lst[low], int)):
                res_lst.append(nested_lst[low])
                low += 1
            else: # lst at low is a list
                temp = flat_list(nested_lst[low], 0 , len(nested_lst[low])-1)
                res_lst.extend(temp)
                low +=1
        return res_lst

def appearances(s, low, high):
    if len(s) ==0:
        return {}
    elif low == high:
        return {s[low] : 1}
    else:
        temp = appearances(s, low, high-1)

        if s[high] in temp:
            temp[s[high]] +=1
        else:
            temp.update({s[high] : 1})
    return temp
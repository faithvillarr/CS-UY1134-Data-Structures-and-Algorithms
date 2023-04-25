# Runtime: Aim for linear

def two_sum(srt_lst, target):
    low = 0
    high = len(srt_lst)-1
    while low <= high:
        if srt_lst[low] + srt_lst[high] == target: #if they add to target
            result = (low, high)
            return result
        elif srt_lst[low] + srt_lst[high] > target: #if too big
            high -= 1
        else: #if too small
            low += 1
    return None


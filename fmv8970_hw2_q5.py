# order list so that all odd #res_stack appear first, followed by all even
# linear runtime.

# resulting runtime is theta(n/20 = theta(n)

def split_parity(lst):
    low = 0
    high = len(lst) - 1
    n = 10
    cnt = 0
    while low <= high:
        cnt += 1
        print("Count = " + str(cnt))
        if lst[low] % 2 == 1:
            low += 1
        elif lst[high] % 2 == 1:
            lst[low], lst[high] = lst[high], lst[low]
            low += 1
            high -= 1
        else:
            high -= 1
    return lst

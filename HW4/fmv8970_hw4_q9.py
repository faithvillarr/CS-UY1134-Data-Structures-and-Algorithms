import copy


def permutations(lst, low, high):
    if low == high:
        perm = [[lst[low]]]
        return perm
    else:
        temp = permutations(lst, low, high - 1)
        perm = []
        for i in range(high - low + 1):
            perm += copy.deepcopy(temp)
        i = 0
        j = 0
        while i < len(perm):
            perm[i].insert(j, lst[high])
            i += 1
            if i % len(temp) == 0:
                j += 1
        return perm


def my_permutations(lst, low, high):
    if low == high:
        res_lst = [[lst[high]]]
        return res_lst
    else:
        res_lst = []
        temp = my_permutations(lst, low + 1, high)
        for i in range(high - low + 1):
            res_lst += copy.deepcopy(temp)
        # i = 0
        j = 0
        # while (i < len(res_lst)):
        for i in range(len(res_lst) + 1):
            print(str(i) + "  " + str(low) + "\n here is len(res_lst) = " + str(len(res_lst)))
            res_lst[i].insert(j, lst[low])
            i += 1
            if i % len(temp) == 0:
                j += 1
            i -= 1
        return res_lst


def main():
    lst = [1, 2, 3]
    print(permutations(lst, 0, len(lst) - 1))
    print(my_permutations(lst, 0, len(lst) - 1))


main()

def my_search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    p1 = 0
    p2 = len(nums)
    while p2 - p1 > 1:
        mid = (p1 + p2) // 2
        print("p1 = " + str(p1) + "\np2 = " + str(p2) + "\nmid= " + str(mid))
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            p1 = mid
        else:
            p2 = mid
    return -1


def main():
    lst = [-1, 0, 3, 5, 9, 12]
    tar = 2
    print(my_search(lst, tar))


main()
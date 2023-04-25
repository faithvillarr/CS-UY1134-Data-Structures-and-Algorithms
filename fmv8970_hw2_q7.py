def findChange(lst01):
    low = 0
    high = len(lst01) - 1
    while low <= high:
        mid = (low+high) //2
        if (lst01[mid] == 1 and (mid ==0 or lst01[mid-1]==0)): # edge cases :(
            return mid
        elif lst01[mid] == 1:
            high = mid-1
        else:
            low = mid+1

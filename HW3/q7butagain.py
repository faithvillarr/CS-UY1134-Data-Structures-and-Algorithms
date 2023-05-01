def findChange(lst01):

    left = 0

    right = len(lst)-1

    while (left <= right):

       middle = (left + right)// 2

       if (lst01[middle] == 1 and (middle == 0 or lst01[middle - 1] == 0)):

         return middle

       elif (lst01[middle] == 1):

         right = middle - 1

       else:

         left = middle + 1

    return None;

lst = [0,0,1]

print(findChange(lst))


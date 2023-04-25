def selection_sort(lst):
    for i in range(len(lst)):
        min = i
        for j in range(i+1, len(lst)):
            if lst[min] > lst[j]:
                min = j
        lst [min], lst[i] = lst[i], lst[min]
    return lst

def insertion_sort(lst):
    for i in range(len(lst)):
        key = lst[i]
        j = i
        while j >=1 and key < lst[j-1]:
            lst[j] = lst[j-1]
            j-=1
        lst[j] = key
    return lst

def merge_sort(lst):
    pass

def merge(lst):
    pass


def power(b, p):
    if p ==0:
        return 1
    else:
        p = power(b,p-1)
        return p * b

def main():
    for i in range(5):
        print(i)


main()
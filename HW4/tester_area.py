#q 4
def main():
    lst1= [1]
    lst2= [3,2,1432,42,654,2,-1,-12312,-12321,131,-2]
    lst3 = []
    lst4 = [-5,-2]
    print(list_min(lst1, 0, len(lst1)-1))
    print(list_min(lst2, 0, len(lst2)-1))
    print(list_min(lst3, 0, len(lst3)-1))
    print(list_min(lst4, 0, len(lst4)-1))

main()


def check_count_lowercase():
    lst1 = "A"
    lst2 = "-sads"
    lst3 = "ANUIEW"
    lst4 = "23"
    print(count_lowercase(lst1, 0, len(lst1)-1))
    print(count_lowercase(lst2, 0, len(lst2)-1))
    print(count_lowercase(lst3, 0, len(lst3)-1))
    print(count_lowercase(lst4, 0, len(lst4)-1))

def main():
    str1 = "aaa"
    str2 = "a-a"
    str3 = "aa"
    str4 = " "
    str5 = ""
    print(is_number_of_lowercase_even(str1, 0, len(str1)-1))
    print(is_number_of_lowercase_even(str2, 0, len(str2)-1))
    print(is_number_of_lowercase_even(str3, 0, len(str3)-1))
    print(is_number_of_lowercase_even(str4, 0, 0))
    print(is_number_of_lowercase_even(str5, 0, 0))


main()




def flat_list(nested_lst, low, high):
    if len(nested_lst) == 0:
        return nested_lst[low]
    elif low == high: # if theres one element in the list
        return nested_lst[low]
    else:
        if isinstance(nested_lst[0], list):
            return flat_list(nested_lst[low], 0, len(nested_lst[low])-1) + flat_list(nested_lst, low+1, len(nested_lst)-1)
        return nested_lst[:1] + (flat_list(nested_lst, low+1, high))




def main():
    lst = [1,2,[3,[4,5]]]
    lst1 = (1,[2,3],[4,[5,6,[7]]],[8])
    print(flat_list(lst, 0, 3))




main()


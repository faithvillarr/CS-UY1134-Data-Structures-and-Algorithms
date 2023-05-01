#part a
def print_triangle(n):
    if n ==0:
        return ""
    else:
        res_str = "*" + print_triangle(n-1)
        print(res_str)
        return res_str

#part b
def print_oposite_triangles(n):
    if n == 0:
        return ""
    else:
        lst = ["*"]*n
        str = "".join(lst)
        print(str)
        print_oposite_triangles(n - 1)
        print(str)

#part c
def print_ruler(n):
    if n == 1:
        print("-")
    else:
        print_ruler(n-1)
        print("-"*n)
        print_ruler(n-1)


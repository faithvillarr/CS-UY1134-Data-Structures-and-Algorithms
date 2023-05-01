# create a postfix calculator.
# works for arithmetic expressions *and* assignment expressions
from ArrayStack import ArrayStack

u_input = ""
u_dict = {}
while True:
    need_assign = False
    u_input = input("--> ")
    if u_input == "done()":
        break

    temp_lst = u_input.split("=")
    u_var = None
    if len(temp_lst) > 1:
        u_var = temp_lst[0].strip()
        u_lst = temp_lst[1].strip().split(" ")
        need_assign = True
    else:
        u_lst = u_input.split(" ")

    s = ArrayStack()
    operators = "+-*/"

    for i in range(len(u_lst)):
        if u_lst[i] in u_dict:
            u_lst[i] = str(u_dict[u_lst[i]])

    for p1 in u_lst:
        if p1 not in operators:          # its an integer
            s.push(p1)
        elif p1 in operators:            # its an operator
            val1 = int(s.pop())
            val2 = int(s.pop())
            if p1 == "+":
                s.push(val1 + val2)
            elif p1 == "-":
                s.push(val2 - val1)
            elif p1 == "*":
                s.push(val1 * val2)
            elif p1 == "/":
                s.push(val2 / val1)
        else:  # is alpha
            if p1 in u_dict.keys():
                s.push(u_dict[p1])

    res = s.pop()  # prints results

    if need_assign:
        u_dict[u_var] = res
        print(u_var)
    else:
        print(res)
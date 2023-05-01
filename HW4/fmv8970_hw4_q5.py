# part a
def count_lowercase(s,low, high):
    if(low > high):
        return 0
    else:
        if s[low].islower():
            return 1 + count_lowercase(s, low+1, high)
        else:
            return count_lowercase(s, low+1, high)

def is_number_of_lowercase_even(s,low,high):
    # need to return a bool
    if low == high:
        if len(s) == 0 or not s.isalpha():
            return False
        elif s[low].islower():    #if it is a vowel, then vowel count is now at 1 and bool = false
            return False
        else:
            return True         #if it is not a vowel, then vowel count is now at 0 and bool = true
    else:
        if s[low].islower():
            return not is_number_of_lowercase_even(s, low+1, high)
        else:
            return is_number_of_lowercase_even(s, low+1, high)

# approximate e to the sum of n + 1.
# Runtime: Linear = theta( n )

def e_approx(n):
    e = 1
    old_val = 1
    for i in range(1, n+1):
        new_factor = 1/i
        new_add = old_val * new_factor
        e += new_add
        old_val = new_add
    return e


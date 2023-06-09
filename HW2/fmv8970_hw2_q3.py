# With runtime of theta(sqrt(num)), return the factors of num in ascending ord

def factors(num):
    for i in range(1, int(num**0.5)+1):
        if num%i==0:
            yield i
    for i in range(int(num**0.5)-1, 0, -1):
        if num%i==0:
            yield num//i

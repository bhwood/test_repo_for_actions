
def is_even(num):
    return num % 2 == 0

def some(num_list, func):
    return any( [ func(i) for i in num_list ] )


    
def every(num_list, func):
    return_val = all([func(i) for i in num_list])
    #return_val = True
    #for i in num_list:
    #    if func(i) is False:
    #        return_val = False

    return return_val
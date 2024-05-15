from src.every import every
#
#Write a function called every that takes a list 
#and a predicate function. 
#A predicate function is one that returns either True or False.
#
#The every function should invoke the predicate function 
#once for each element in the list. 
#Each time it is invoked, the current element of the list 
#should be passed as an argument to the predicate.
#
#If the predicate function returns True for all elements 
#of the list ,then the every function should return True. 
#Otherwise, it should return False
def is_even(num):
    return num % 2 == 0

def test_returns_true_or_false():
    input_1 = ([1,2,3] , is_even)
    result = every(*input_1)
    #expected = True or False
    assert result.__class__ == bool

def test_returns_false_for_list_when_numbers_not_all_even():
    input_1 = ([1,5,2,8] , is_even)
    result = every(*input_1)
    #expected = True or False
    assert result == False

def test_returns_true_for_list_of_even_numbers():
    input_1 = ([6,2,8] , is_even)
    result = every(*input_1)
    #expected = True or False
    assert result == True
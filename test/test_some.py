from src.some import some is_even

# func called some
# args: list, predicate function
# method: invoke predicate function once for each element in list
# return: True if func returns Tur at least once else False 
#
def test_returns_true_or_false():
    input_1 = ([1,2,3] , is_even)
    result = some(*input_1)
    assert result.__class__ == bool

def test_returns_false_when_all_numbers_in_list_are_odd():
    input_1 = ([1,5,3] , is_even)
    result = some(*input_1)
    #expected = True or False
    assert result == False

def test_returns_true_when_list_contains_any_even_number():
    input_1 = ([6,5,3] , is_even)
    result = some(*input_1)
    #expected = True or False
    assert result == True


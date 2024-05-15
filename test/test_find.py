import pytest
from src.find import find, is_multiple_of_five

# test original list unchanged
@pytest.mark.xfail(reason="purposefully creating a fail to prove test function")
def test_input_not_mutated():
    input1 = [1,2,3]
    expected = input1.copy()
    def test_func(): pass
    _ = find(input1, test_func)
    assert input1 == expected



# test function returns integer
def test_function_returns_an_integer():
    input_1 = ([1,2,3] , is_multiple_of_five)
    result = find(*input_1)
    assert result.__class__ is int
    
# test predicate function has been invoked
def test_predicate_function_has_been_invoked():
    is_invoked = False
    input_1 = ([1,2,3] , is_multiple_of_five)
    def test_func():
        nonlocal is_invoked
        is_invoked = True
    _ = find(*input_1)
    assert is_invoked is True
# test function returns an integer which is a multiple of five

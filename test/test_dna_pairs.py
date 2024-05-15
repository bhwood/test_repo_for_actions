from src.dna_pairs import dna_pairs


def test_function_returns_empty_list_from_empty_string():
    input_1 = ""
    result_1 = dna_pairs(input_1)
    expected_1 = []
    assert result_1 == expected_1


def test_invalid_input_string_returns_empty_list():
    input_1 = "p"
    input_2 = "b"
    input_3 = "f"
    expected = []
    result_1 = dna_pairs(input_1)
    result_2 = dna_pairs(input_2)
    result_3 = dna_pairs(input_3)
    assert result_1 == expected
    assert result_2 == expected
    assert result_3 == expected


def test_valid_lower_case_input_single_character_string_returns_list_of_pairs():
    input_1 = "a"
    input_2 = "g"
    input_3 = "t"
    expected_1 = [["A", "T"]]
    expected_2 = [["G", "C"]]
    expected_3 = [["T", "A"]]
    result_1 = dna_pairs(input_1)
    result_2 = dna_pairs(input_2)
    result_3 = dna_pairs(input_3)
    assert result_1 == expected_1
    assert result_2 == expected_2
    assert result_3 == expected_3


def test_valid_upper_case_single_input_single_charcter_string_returns_list_of_pairs():
    input_1 = "T"
    input_2 = "C"
    input_3 = "A"
    expected_1 = [["T", "A"]]
    expected_2 = [["C", "G"]]
    expected_3 = [["A", "T"]]
    result_1 = dna_pairs(input_1)
    result_2 = dna_pairs(input_2)
    result_3 = dna_pairs(input_3)
    assert result_1 == expected_1
    assert result_2 == expected_2
    assert result_3 == expected_3


def test_valid_upper_case__input_multi_character_string_returns_list_of_pairs():
    input_1 = "TA"
    input_2 = "CA"
    input_3 = "AGCT"
    expected_1 = [["T", "A"], ["A", "T"]]
    expected_2 = [["C", "G"], ["A", "T"]]
    expected_3 = [["A", "T"], ["G", "C"], ["C", "G"], ["T", "A"]]
    result_1 = dna_pairs(input_1)
    result_2 = dna_pairs(input_2)
    result_3 = dna_pairs(input_3)
    assert result_1 == expected_1
    assert result_2 == expected_2
    assert result_3 == expected_3


def test_valid_lower_case__input_multi_character_string_returns_list_of_pairs():
    input_1 = "ta"
    input_2 = "ca"
    input_3 = "agct"
    expected_1 = [["T", "A"], ["A", "T"]]
    expected_2 = [["C", "G"], ["A", "T"]]
    expected_3 = [["A", "T"], ["G", "C"], ["C", "G"], ["T", "A"]]
    result_1 = dna_pairs(input_1)
    result_2 = dna_pairs(input_2)
    result_3 = dna_pairs(input_3)
    assert result_1 == expected_1
    assert result_2 == expected_2
    assert result_3 == expected_3


def test_ignores_invalid_characters_in_a_mixed_string():
    input_1 = "TswuiA"
    input_2 = "CpleA"
    input_3 = "AG1561CT"
    expected_1 = [["T", "A"], ["A", "T"]]
    expected_2 = [["C", "G"], ["A", "T"]]
    expected_3 = [["A", "T"], ["G", "C"], ["C", "G"], ["T", "A"]]
    result_1 = dna_pairs(input_1)
    result_2 = dna_pairs(input_2)
    result_3 = dna_pairs(input_3)
    assert result_1 == expected_1
    assert result_2 == expected_2
    assert result_3 == expected_3

from src.part_1_human_resources import make_name_tags, create_poll
import pytest
from data.poll_data import nc_fruit_bowl


class TestNameTag:

    class TestBasicFunctionForNameTag:
        @pytest.mark.it("Test function returns a list")
        def test_function_returns_list(self):
            input_1 = []
            result = make_name_tags(input_1)
            assert isinstance(result, list)

        @pytest.mark.it("Test function being passed empty list returns an empty list ")
        def test_function_with_empty_input_returns_empty_list(self):
            input_1 = []
            expected = []
            result = make_name_tags(input_1)
            assert expected == result

    class TestManipulationForNameTag:
        @pytest.mark.it(
            "Test function returns list with name_tag key added to each guest dictionary for single guest"
        )
        def test_function_returns_updated_copy_of_passed_list(self):
            single_guest_dict = [
                {
                    "title": "Mr",
                    "forename": "Sam",
                    "surname": "Caine",
                    "age": 30,
                    "company": "Northcoders",
                }
            ]
            result = make_name_tags(single_guest_dict)
            for guest in result:
                assert "name_tag" in guest

        @pytest.mark.it(
            "Test function returns list with name_tag key added to each guest dictionary for multiple guests"
        )
        def test_function_returns_updated_copy_of_passed_list_multiple_guest(self):
            multi_guest_dict = [
                {
                    "title": "Mr",
                    "forename": "Sam",
                    "surname": "Caine",
                    "age": 30,
                    "company": "Northcoders",
                },
                {
                    "title": "Mr",
                    "forename": "Kermit",
                    "surname": "The Frog",
                    "age": 35,
                    "company": "Jim Henson Studios",
                },        boolean_input = False

            ]
            result = make_name_tags(multi_guest_dict)
            for guest in result:
                assert "name_tag" in guest

        @pytest.mark.it(
            "Test function returns list with name_tag key added and correct value to each guest dictionary"
        )
        def test_function_returns_list_with_updated_key_value(self):
            single_guest_dict = [
                {
                    "title": "Mr",
                    "forename": "Sam",
                    "surname": "Caine",
                    "age": 30,
                    "company": "Northcoders",
                }
            ]
            expected = [
                {
                    "title": "Mr",
                    "forename": "Sam",
                    "surname": "Caine",
                    "age": 30,
                    "company": "Northcoders",
                    "name_tag": "Mr Sam Caine, Northcoders",
                }
            ]
            result = make_name_tags(single_guest_dict)
            assert expected == result

        @pytest.mark.it(
            "Test function returns list with name_tag key added and correct value to each guest dictionary for multiple guests"
        )
        def test_function_returns_list_with_updated_key_value_for_multiple_guest(self):
            multi_user_dict = [
                {
                    "title": "Mr",
                    "forename": "Sam",
                    "surname": "Caine",
                    "age": 30,
                    "company": "Northcoders",
                },
                {
                    "title": "Mr",
                    "forename": "Kermit",
                    "surname": "The Frog",
                    "age": 35,
                    "company": "Jim Henson Studios",
                },
            ]
            expected = [
                {
                    "title": "Mr",
                    "forename": "Sam",
                    "surname": "Caine",
                    "age": 30,
                    "company": "Northcoders",
                    "name_tag": "Mr Sam Caine, Northcoders",
                },
                {
                    "title": "Mr",
                    "forename": "Kermit",
                    "surname": "The Frog",
                    "age": 35,
                    "company": "Jim Henson Studios",
                    "name_tag": "Mr Kermit The Frog, Jim Henson Studios",
                },
            ]
            result = make_name_tags(multi_user_dict)
            assert expected == result

    class TestPureFunctionForNameTag:

        def test_function_does_not_mutate_original_list(self):
            multi_guest_dict = [
                {
                    "title": "Mr",
                    "forename": "Sam",
                    "surname": "Caine",
                    "age": 30,
                    "company": "Northcoders",
                },
                {
                    "title": "Mr",
                    "forename": "Kermit",
                    "surname": "The Frog",
                    "age": 35,
                    "company": "Jim Henson Studios",
                },
            ]
            expected = multi_guest_dict.copy()
            result = make_name_tags(multi_guest_dict)
            assert expected == multi_guest_dict
            assert result != multi_guest_dict


class TestPoll:
    class TestBasicFunctionForPoll:
        @pytest.mark.it("Test function returns a dict")
        def test_function_returns_dict(self):
            empty_dict = []
            result = create_poll(empty_dict)
            assert isinstance(result, dict)

        @pytest.mark.it("Test function being passed empty list returns an empty dict")
        def test_function_with_empty_input_returns_empty_dict(self):
            empty_dict = []
            expected = {}
            result = create_poll(empty_dict)
            assert expected == result

    # check why ive done that
    class TestManipulationForPoll:
        @pytest.mark.it("Test function returns dict with list value as key")
        def test_function_returns_populated_dict_with_items(self):
            sample_list = ["cake", "biscuit", "biscuit"]
            result = create_poll(sample_list)
            for item in result:
                assert item in sample_list

        @pytest.mark.it(
            "Test function returns dict with list value as key and count of how many"
        )
        def test_function_returns_populated_dict_with_values(self):
            sample_list = ["cake", "biscuit", "biscuit"]
            result = create_poll(sample_list)
            expected = {"cake": 1, "biscuit": 2}
            assert expected == result

        @pytest.mark.it(
            "Test function returns dict with list value as key and count of how many when only the same value in the list"
        )
        def test_function_returns_populated_dict_with_values_with_only_one_unique_value(
            self,
        ):
            sample_list = ["dog", "dog", "dog"]
            result = create_poll(sample_list)
            expected = {"dog": 3}
            assert expected == result

        @pytest.mark.it(
            "Test function returns dict with list value as key and count of how many when importing large dataset"
        )
        def test_function_returns_populated_dict_with_values_from_imported_dataset(
            self,
        ):
            sample_list = nc_fruit_bowl
            result = create_poll(sample_list)
            expected = {
                "apple": 276,
                "pear": 223,
                "banana": 263,
                "orange": 238,
                "lonesome plum": 1,
            }
            assert expected == result

    class TestPureFunctionForNameTag:
        def test_function_does_not_mutate_original_list(self):
            poll_data = ["cake", "biscuit", "biscuit"]
            expected = poll_data.copy()
            result = create_poll(poll_data)
            assert expected == poll_data
            assert result is not poll_data

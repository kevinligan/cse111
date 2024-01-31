from names import make_full_name, \
    extract_given_name, extract_family_name
import pytest


def test_make_full_name():
    # Test make_full_name with various names
    assert make_full_name("John", "Doe") == "Doe;John"
    assert make_full_name("Alice", "Johnson") == "Johnson;Alice"
    assert make_full_name("Bob", "Smith-Jones") == "Smith-Jones;Bob"
    assert make_full_name("", "") == ";"
    # Add more test cases as needed

def test_extract_family_name():
    # Test extract_family_name with various names
    assert extract_family_name("Doe; John") == "Doe"
    assert extract_family_name("Johnson; Alice") == "Johnson"
    assert extract_family_name("Smith-Jones; Bob") == "Smith-Jones"
    assert extract_family_name("; ") == ""
    # Add more test cases as needed

def test_extract_given_name():
    # Test extract_given_name with various names
    assert extract_given_name("Doe; John") == "John"
    assert extract_given_name("Johnson; Alice") == "Alice"
    assert extract_given_name("Smith-Jones; Bob") == "Bob"
    assert extract_given_name("; ") == ""
    # Add more test cases as needed

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
if __name__ == "__main__":
    pytest.main(["-v", "--tb=line", "-rN", __file__])

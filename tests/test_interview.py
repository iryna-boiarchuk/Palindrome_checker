import pytest

from interview_package.interview_module import (
    check_palindrome,
    validate_value,
    transform_string
)
from interview_package.exceptions import (
    InvalidStringMinLength,
    InvalidStringMaxLength,
    UnsupportedStringChar,
    InvalidStringType,
    EmptyStringError
)


# Test validate_value function
def test_validate_value_valid_cases():
    validate_value("abc")  # Valid string
    validate_value("123")  # Valid numeric string
    validate_value("AbC123")  # Mixed alphanumeric
    validate_value("Aba")  # Valid palindrome


def test_validate_value_invalid_type():
    with pytest.raises(InvalidStringType):
        validate_value(123)  # Not a string
    with pytest.raises(InvalidStringType):
        validate_value(None)  # NoneType
    with pytest.raises(InvalidStringType):
        validate_value([])  # List input


def test_validate_value_min_length():
    with pytest.raises(InvalidStringMinLength):
        validate_value("a")  # Less than 2 characters
    with pytest.raises(InvalidStringMinLength):
        validate_value("")  # Empty string


def test_validate_value_max_length():
    with pytest.raises(InvalidStringMaxLength):
        validate_value("a" * 16)  # More than 15 characters


def test_validate_value_special_characters():
    with pytest.raises(UnsupportedStringChar):
        validate_value("abc!")
    with pytest.raises(UnsupportedStringChar):
        validate_value("123@")
    with pytest.raises(UnsupportedStringChar):
        validate_value("%1abc&")


def test_validate_value_empty_string_with_whitespaces():
    with pytest.raises(EmptyStringError):
        validate_value("   ")


def test_transform_string():
    assert transform_string(' Lost ') == 'lost'
    assert transform_string('  IrynA') == 'iryna'
    assert transform_string('Max   ') == 'max'

# Test check_palindrome function
def test_check_palindrome_valid_palindromes():
    assert check_palindrome("aba") is True
    assert check_palindrome("Aba") is True
    assert check_palindrome("12321") is True
    assert check_palindrome("Aba  ") is True
    assert check_palindrome("  Aba") is True


def test_check_palindrome_invalid_palindromes():
    assert check_palindrome("abca") is False
    assert check_palindrome("abc123") is False
    assert check_palindrome("12345") is False


def test_check_palindrome_invalid_input():
    with pytest.raises(InvalidStringType):
        check_palindrome(123)  # not a string
    with pytest.raises(InvalidStringMinLength):
        check_palindrome("a")  # less than 2 characters
    with pytest.raises(InvalidStringMaxLength):
        check_palindrome("a" * 16)  # more than 15 characters
    with pytest.raises(UnsupportedStringChar):
        check_palindrome("abc!")  # contains special character
    with pytest.raises(EmptyStringError):
        check_palindrome("   ")  # only whitespaces

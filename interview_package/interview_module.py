# 'aba' -> True
# 'abca' -> False
# Check if a given string is a palindrome
from interview_package.exceptions import (
    InvalidStringMinLength,
    InvalidStringMaxLength,
    UnsupportedStringChar,
    InvalidStringType,
    EmptyStringError
)


def check_palindrome(input_str: str) -> bool:
    """ Return whether the string is a palindrome. """
    validate_value(input_str)
    res_str = transform_string(input_str)
    return res_str == res_str[::-1]


def transform_string(string: str) -> str:
    return string.lower().strip()


def validate_value(string_value: str):
    """ Validate the received string value to raise specific exceptions for specific use cases """
    # validate if string has supported type and length
    if not isinstance(string_value, str):
        raise InvalidStringType('Input must be a string.')
    if len(string_value) < 2:
        raise InvalidStringMinLength('Inputs must be at least two characters long.')
    if len(string_value) > 15:
        raise InvalidStringMaxLength('Input must be less than 15 characters.')

    # validate if string contains only whitespaces
    if string_value.strip() == '':
        raise EmptyStringError('Input can not contain only whitespaces.')

    # validate if string contains special characters
    for char in string_value:
        if not char.isalnum() and not char.isspace():
            raise UnsupportedStringChar('Special characters are not allowed.')

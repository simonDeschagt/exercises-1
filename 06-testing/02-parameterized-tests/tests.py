import pytest
from parentheses import matching_parentheses 


@pytest.mark.parametrize('string', [
    '((1, 5), (3, 6))',
    # '((1, 5), (5, 6)',
    # '((1, 10), 3, 6))',
    # '((6, 8, (3, 6))',
    # '(5, 7), (4, 8))',
])
def test_if_the_parentheses_do_match(string):
    assert matching_parentheses(string), f"the string has a correct amount of parentheses."

@pytest.mark.parametrize('string', [
    # '((1, 5), (3, 6))',
    '((1, 5), (5, 6)',
    '((1, 10), 3, 6))',
    '((6, 8, (3, 6))',
    '(5, 7), (4, 8))',
    ')(',
])
def test_if_the_parentheses_do_not_match(string):
    assert not matching_parentheses(string), f"The string has a correct amount of parentheses."
import pytest
from book import Book 



@pytest.mark.parametrize('title', [
    "Watchmen",
    "hunger games",
    "bladerunner",
])
@pytest.mark.parametrize('isbn', [
    '978-1779501127',
    '978-17795011-27',
    '9781779501127',
    '9781 7795 01127',

])
def test_valid_creation(title, isbn):
    b = Book(title, isbn)

    assert b.title == title      
    assert b.isbn == isbn

@pytest.mark.parametrize('wrong_title', [
    "",
])
@pytest.mark.parametrize('isbn', [
    '978-1779501127',
    '978-17795011-27',
    '9781779501127',
    '9781 7795 01127',
])
def test_creation_with_invalid_title(wrong_title, isbn):
    with pytest.raises(RuntimeError):
        Book(wrong_title, isbn)

@pytest.mark.parametrize('title', [
    "Watchmen",
    "hunger games",
    "bladerunner",
])
@pytest.mark.parametrize('wrong_isbn', [
    '978-1779501126',
    '9780735611331',
    '978-1709571127',
    '978-1-77-950182-7',
    '97817795011271',
    '978073561131'
])
def test_creation_with_invalid_isbn(title, wrong_isbn):
    with pytest.raises(RuntimeError):
        Book(title, wrong_isbn)
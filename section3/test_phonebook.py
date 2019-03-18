import pytest


from phonebook import Phonebook


@pytest.fixture
def phonebook(tmpdir):
    phone_book = Phonebook(tmpdir)
    return phone_book


# @pytest.skip("WIP") # Skips all tests below this point
def test_add_and_lookup_entry(phonebook):
    # pytest.skip("WIP")
    phonebook = Phonebook()
    phonebook.add("Bob", "123")
    assert "123" == phonebook.lookup("Bob")


def test_phonebook_gives_access_to_names_and_numbers(phonebook):
    phonebook = Phonebook()
    phonebook.add("Alice", "12345")
    phonebook.add("Bob", "123")
    assert set(phonebook.names()) == {"Alice", "Bob"}
    assert "12345" in phonebook.numbers()


def test_missing_entry_raises_KeyError(phonebook):
    phonebook = Phonebook()
    with pytest.raises(KeyError):
        phonebook.lookup("missing")


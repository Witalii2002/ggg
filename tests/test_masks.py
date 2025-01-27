import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.fixture
def data_test():
    return "1234567890123456"


def test_get_mask_card_number(data_test):
    assert get_mask_card_number(data_test) == "1234 56** **** 3456"


def test_get_mask_card_number_empty():
    assert get_mask_card_number("") == "Invalid card number length"


def test_get_mask_account(data_test):
    assert get_mask_account(data_test) == "**3456"


def test_get_mask_account_empty():
    assert get_mask_account("") == "Invalid account number length"

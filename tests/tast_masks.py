import pytest
from src.masks import get_mask_card_number, get_mask_account  # Импортируем функции из вашего файла

# ----- Тесты для get_mask_card_number -----

def test_get_mask_card_number_valid():
    card_number = "1234567890123456"
    expected_mask = "1234 56** **** 3456"
    assert get_mask_card_number(card_number) == expected_mask

def test_get_mask_card_number_invalid_length_short():
    card_number = "123456789012345"  # 15 digits
    assert get_mask_card_number(card_number) == "Invalid card number length"

def test_get_mask_card_number_invalid_length_long():
    card_number = "12345678901234567"  # 17 digits
    assert get_mask_card_number(card_number) == "Invalid card number length"

def test_get_mask_card_number_numeric_input():
    card_number = 1234567890123456  # Integer input
    expected_mask = "1234 56** **** 3456"
    assert get_mask_card_number(card_number) == expected_mask

def test_get_mask_card_number_with_spaces():
    card_number = "1234 5678 9012 3456"  # Input with spaces
    assert get_mask_card_number(card_number) == "Invalid card number length" # spaces makes the length > 16

# ----- Тесты для get_mask_account -----

def test_get_mask_account_valid():
    account_number = "1234567890"
    expected_mask = "**7890"
    assert get_mask_account(account_number) == expected_mask

def test_get_mask_account_short():
    account_number = "123"
    assert get_mask_account(account_number) == "Invalid account number length"

def test_get_mask_account_numeric_input():
    account_number = 1234567890
    expected_mask = "**7890"
    assert get_mask_account(account_number) == expected_mask

def test_get_mask_account_exact_length():
    account_number = "1234"
    expected_mask = "**1234"
    assert get_mask_account(account_number) == expected_mask

def test_get_mask_account_long():
     account_number = "12345678901234567890" #20 digits.
     expected_mask = "**7890"
     assert get_mask_account(account_number) == expected_mask
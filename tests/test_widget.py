import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "input_mask, output_mask",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("", "Invalid input format"),
    ],
)
def test_mask_account_card(input_mask, output_mask):
    assert mask_account_card(input_mask) == output_mask


@pytest.mark.parametrize(
    "input_time, output_time", [("2024-03-11T02:26:18.671407", "11.03.2024"), ("", "Invalid date format")]
)
def test_get_date(input_time, output_time):
    assert get_date(input_time) == output_time

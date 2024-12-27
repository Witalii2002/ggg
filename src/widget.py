from masks import get_mask_account, get_mask_card_number


def mask_account_card(input_string: str) -> str:
    """Возвращать строку с замаскированным номером."""
    if "Счет" in input_string:
        try:
            parts = input_string.split("Счет ", 1)  # Split only once
            account_number = parts[1].strip()
            return "Счет " + str(get_mask_account(account_number))  # Include type in output
        except IndexError:
            return "Invalid input format"

    else:
        try:
            parts = input_string.rsplit(" ", 1)  # split only once from the right side
            card_type = parts[0].strip()
            card_number = parts[1].strip()

            return f"{card_type} {get_mask_card_number(card_number)}"  # Include type in output
        except (IndexError, ValueError):
            return "Invalid input format"


def get_date(date_string: str) -> str:
    """возвращает строку с датой в формате  "ДД.ММ.ГГГГ" """

    try:
        year = int(date_string[0:4])
        month = int(date_string[5:7])
        day = int(date_string[8:10])

        # Crucial: Ensure month and day are within valid ranges.
        if not (1 <= month <= 12 and 1 <= day <= 31):
            return "Invalid date format"

        return f"{day}.{month}.{year}"
    except (ValueError, IndexError):
        return "Invalid date format"

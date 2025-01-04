def get_mask_card_number(card_number: str) -> str:
    """принимает на вход номер карты и возвращает ее маску"""
    card_number = str(card_number)  # Ensure card_number is a string
    if len(card_number) != 16:
        return "Invalid card number length"

    masked_card = card_number[:4] + " " + card_number[4:6] + "** **** " + card_number[-4:]
    return masked_card


def get_mask_account(account_number: str) -> str:
    """принимает на вход номер счета и возвращает его маску"""
    account_number = str(account_number)  # Ensure account_number is a string
    if len(account_number) < 4:
        return "Invalid account number length"

    masked_account = "**" + account_number[-4:]
    return  masked_account

import masks

def mask_account_card(input_string: str) -> str:
    """ """
    if "Счет" in input_string:
      parts = input_string.split("Счет ")
      if len(parts) < 2:
          return "Invalid input format"
      account_number = parts[1].strip()
      return masks.get_mask_account(account_number)

    else:
      parts = input_string.split(" ")
      if len(parts) < 2:
          return "Invalid input format"
      card_number = parts[-1].strip()
      return masks.get_mask_card_number(card_number)
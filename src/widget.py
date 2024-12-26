import masks

def mask_account_card(input_string: str) -> str:
    """Возвращать строку с замаскированным номером """
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

    def get_date(date_string):
        """возвращает строку с датой  """

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
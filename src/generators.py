def filter_by_currency(transactions, currency_code):
    """Возвращает итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной (например, USD)"""
    for transaction in transactions:
        try:
            if transaction['operationAmount']['currency']['code'] == currency_code:
                yield transaction
        except (KeyError, TypeError):
            continue


def transaction_descriptions(transactions):
    """Принимает список словарей с транзакциями и возвращает описание каждой операции по очереди"""
    for transaction in transactions:
        try:
            yield transaction['description']
        except KeyError:
            yield "Описание отсутствует"


def card_number_generator(start, end):
    """Выдает номера банковских карт в формате XXXX XXXX XXXX XXXX"""
    for i in range(start, end + 1):
        card_number = str(i).zfill(16)  # Заполняем нулями до 16 цифр
        formatted_card_number = " ".join([card_number[j:j+4] for j in range(0, 16, 4)])
        yield formatted_card_number

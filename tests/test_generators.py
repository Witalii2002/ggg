from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


# ----- Тесты для filter_by_currency -----
def test_filter_by_currency_empty_list():
    assert list(filter_by_currency([], "USD")) == []


def test_filter_by_currency_matching_currency():
    transactions = [
        {"operationAmount": {"currency": {"code": "USD"}}},
        {"operationAmount": {"currency": {"code": "EUR"}}},
        {"operationAmount": {"currency": {"code": "USD"}}},
    ]
    expected = [{"operationAmount": {"currency": {"code": "USD"}}}, {"operationAmount": {"currency": {"code": "USD"}}}]
    assert list(filter_by_currency(transactions, "USD")) == expected


def test_filter_by_currency_no_matching_currency():
    transactions = [
        {"operationAmount": {"currency": {"code": "EUR"}}},
        {"operationAmount": {"currency": {"code": "GBP"}}},
    ]
    assert list(filter_by_currency(transactions, "USD")) == []


def test_filter_by_currency_missing_currency_key():
    transactions = [
        {"operationAmount": {"currency": {"code": "USD"}}},
        {"operationAmount": {}},
        {"operationAmount": {"currency": {"code": "USD"}}},
    ]
    expected = [{"operationAmount": {"currency": {"code": "USD"}}}, {"operationAmount": {"currency": {"code": "USD"}}}]
    assert list(filter_by_currency(transactions, "USD")) == expected


def test_filter_by_currency_missing_operationAmount_key():
    transactions = [
        {"operationAmount": {"currency": {"code": "USD"}}},
        {},
        {"operationAmount": {"currency": {"code": "USD"}}},
    ]
    expected = [{"operationAmount": {"currency": {"code": "USD"}}}, {"operationAmount": {"currency": {"code": "USD"}}}]
    assert list(filter_by_currency(transactions, "USD")) == expected


# ----- Тесты для transaction_descriptions -----
def test_transaction_descriptions_empty_list():
    assert list(transaction_descriptions([])) == []


def test_transaction_descriptions_with_descriptions():
    transactions = [
        {"description": "Перевод организации"},
        {"description": "Покупка в магазине"},
        {"description": "Оплата услуг"},
    ]
    expected = ["Перевод организации", "Покупка в магазине", "Оплата услуг"]
    assert list(transaction_descriptions(transactions)) == expected


def test_transaction_descriptions_missing_description():
    transactions = [{"description": "Перевод организации"}, {}, {"description": "Оплата услуг"}]
    expected = ["Перевод организации", "Описание отсутствует", "Оплата услуг"]
    #  Убедитесь, что функция возвращает "Описание отсутствует" когда ключ отсутствует
    assert list(transaction_descriptions(transactions)) == expected


# ----- Тесты для card_number_generator -----
def test_card_number_generator_range():
    expected = ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"]
    assert list(card_number_generator(1, 3)) == expected


def test_card_number_generator_single_value():
    assert list(card_number_generator(10, 10)) == ["0000 0000 0000 0010"]


def test_card_number_generator_start_greater_than_end():
    assert list(card_number_generator(100, 10)) == []  # Пустой список, если начало > конца

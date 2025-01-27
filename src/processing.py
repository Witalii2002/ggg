from datetime import datetime
from typing import Any, Dict, List


def filter_by_state(data: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """Возвращает новый список словарей, содержит те словари, у которых ключ state соответствует указанному значению"""
    filtered_data: List[Dict[str, Any]] = []
    if data == []:
        return []
    for item in data:
        if "state" in item and item["state"] == state:
            filtered_data.append(item)
    return filtered_data


def sort_by_date(data: List[Dict[str, Any]], reverse: bool = True) -> List[Dict[str, Any]]:
    """Возвращать новый список, отсортированный по дате"""
    if data == []:
        return []
    return sorted(data, key=lambda x: datetime.fromisoformat(x["date"]), reverse=reverse)


# print(filter_by_state(data = []))
# print(sort_by_date(data = []))
# print(sort_by_date(data = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
#             {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
#             {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
#             {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
#             ]))

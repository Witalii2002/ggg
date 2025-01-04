from datetime import datetime
from typing import Any, Dict, List


def filter_by_state(input_data: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """функция возвращает новый список словарей, содержащий только те словари, у которых ключ state соответствует
    указанному значению"""
    filtered_data = []
    for item in input_data:
        if "state" in item and item["state"] == state:
            filtered_data.append(item)
    return filtered_data


def sort_by_date(input_data: List[Dict[str, Any]], reverse: bool = True) -> List[Dict[str, Any]]:
    """возвращать новый список, отсортированный по дате"""
    return sorted(input_data, key=lambda x: datetime.fromisoformat(x["date"]), reverse=reverse)

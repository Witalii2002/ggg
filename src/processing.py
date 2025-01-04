from datetime import datetime
from typing import Any, Dict, List


def filter_by_state(data: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """Возвращает новый список словарей, по ключу  state"""
    filtered_data: List[Dict[str, Any]] = []
    for item in data:
        if "state" in item and item["state"] == state:
            filtered_data.append(item)
    return filtered_data


def sort_by_date(data: List[Dict[str, Any]], reverse: bool = True) -> List[Dict[str, Any]]:
    """Возвращать новый список, отсортированный по дате"""
    return sorted(data, key=lambda x: datetime.fromisoformat(x["date"]), reverse=reverse)

from datetime import datetime


def filter_by_state(data, state='EXECUTED'):
    """ """
    filtered_data = []
    for item in data:
        if 'state' in item and item['state'] == state:
            filtered_data.append(item)
    return filtered_data


def sort_by_date(data, reverse=True):
    """ """
    return sorted(data, key=lambda x: datetime.fromisoformat(x['date']), reverse=reverse)

# Example with default sorting (descending)
sorted_data_desc = sort_by_date(data)
print(sorted_data_desc)

# Example with ascending sorting
sorted_data_asc = sort_by_date(data, reverse=False)
print(sorted_data_asc)

# Example Usage:
data = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

# Example with the default state
filtered_executed = filter_by_state(data)
print(filtered_executed)

# Example with a specified state
filtered_canceled = filter_by_state(data, 'CANCELED')
print(filtered_canceled)
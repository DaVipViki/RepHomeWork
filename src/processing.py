def filter_by_state(bank_operations: list , state: str ='EXECUTED') -> list:
    """Функция возвращает новый список словарей, содержащий только те словари, у которых ключ
    state соответствует значению 'EXECUTED'."""
    filtered_by_state = []
    for dict in bank_operations:
        if dict['state'] == state:
            filtered_by_state.append(dict)
    return filtered_by_state

def sort_by_date(bank_operations: list , reverse: bool =True) -> list:
    """ Функция принимает список словарей и необязательный параметр, задающий порядок сортировки
    (по умолчанию — убывание). Функция должна возвращать новый список, отсортированный по дате (
    date)."""
    sorted_by_date_reverse = sorted(bank_operations, key=lambda dict: dict['date'], reverse=reverse)
    return sorted_by_date_reverse

if __name__ == "__main__":
    filtered = filter_by_state([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                                {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                                {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                                {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}],
                               state='CANCELED')
    print(filtered)

    sorted_operation = sort_by_date([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                                {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                                {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                                {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}], reverse=False)
    print(sorted_operation)
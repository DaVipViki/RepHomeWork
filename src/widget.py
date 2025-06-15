from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(type_and_num_card: str) -> str:
    """Функция принимает один аргумент — строку, содержащую тип и номер карты
    или счета и возвращает замаскированную информацию."""
    if "Счет" in type_and_num_card:
        return get_mask_account(type_and_num_card)
    else:
        return get_mask_card_number(type_and_num_card)


def get_date(date: str) -> str:
    """Функция принимает на вход строку с датой в формате
    и возвращает строку с датой в формате ДД.ММ.ГГГГ"""
    return f"{date[8:10]}.{date[5:7]}.{date[:4]}"


if __name__ == "__main__":
    card = mask_account_card("MasterCard 7158300734726758")
    account = mask_account_card("Счет 35383033474447895560")
    print(card)
    print(account)
    short_date = get_date("2024-03-11T02:26:18.671407")
    print(short_date)

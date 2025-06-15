def get_mask_card_number(card_num: str) -> str:
    """Функция возвращает строку с замаскированным номером"""
    two_num = card_num[-12:-10]
    four_num = card_num[-4:]
    first_num = card_num[-16:-12]
    name_card = card_num[:-17]
    mask_num = f"{name_card} {first_num} {two_num}** **** {four_num}"
    return mask_num


def get_mask_account(mask_account: str) -> str:
    """принимает на вход номер счета в виде строки и возвращает маску номера по правилу
    Счет **XXXX"""
    return f"Счет **{mask_account[-4:]}"


if __name__ == "__main__":
    card_number = get_mask_card_number("Maestro 1596837868705199")
    print(card_number)

    account = get_mask_account("Счет 73654108430135874305")
    print(account)

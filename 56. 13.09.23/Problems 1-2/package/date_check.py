def date_check(date: str) -> bool:
    date_lst = date.split(".")
    if len(date_lst) != 3:
        return False
    try:
        date_lst = list(map(int, date_lst))
    except ValueError:
        return False
    if date_lst[2] not in range(1, 10000):
        return False
    if date_lst[1] not in range(1, 13):
        return False
    days = 31
    if date_lst[1] in (4, 6, 9, 11):
        days = 30
    elif date_lst[1] == 2:
        days = leap_year(date_lst[2])
    if date_lst[0] not in range(1, days + 1):
        return False
    return True


def leap_year(year: int) -> int:
    if year % 4 == 0:
        return 29
    else:
        return 28

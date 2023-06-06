from datetime import datetime, date, timedelta


def get_current_day_of_the_week() -> str:
    """
        Gets the current day of the week and returns it
    """
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    return weekdays[datetime.today().weekday()]


def calculate_age(birthday_date: datetime) -> int:
    """
        Calculates the age of the person by his birthday date and returns it
    """
    today = date.today()
    age = today.year - birthday_date.year - ((today.month, today.day) < (birthday_date.month, birthday_date.day))
    return age


def calculate_time_till_birthday(birthday_date: datetime) -> datetime.time:
    """
        Calculates time till the next closest birthday and returns it
    """
    today = datetime.now()
    next_birthday = datetime(birthday_date.year + calculate_age(birthday_date) + 1,\
                            birthday_date.month, birthday_date.day)
    return next_birthday - today


def compute_double_day(b_day1: datetime, b_day2: datetime, n: int=2) -> None:
    """
        Computes double day
    """
    if b_day1 > b_day2:
        start_date = b_day1
    else:
        start_date = b_day2

    for i in range(100*365):
        c_date = start_date + timedelta(days=i)
        d1 = c_date - b_day1
        d2 = c_date - b_day2
        if d1 > d2:
            if d1.days == n*d2.days:
                print(c_date.strftime('%d-%m-%Y'))
        elif d2.days == n*d1.days:
                print(c_date.strftime('%d-%m-%Y'))


def main() -> None:
    """
        The main function in the script
    """
    print(get_current_day_of_the_week())

    birthday = datetime(2002, 3, 18)
    print(calculate_age(birthday))
    print(calculate_time_till_birthday(birthday))

    compute_double_day(birthday, datetime(2012, 8, 22))


if __name__ == "__main__":
    main()

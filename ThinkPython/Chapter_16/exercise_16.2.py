class Time(object):
    """
        Represents the time of day.
        attributes: hour, minute, second
    """


def is_after(time_1: Time, time_2: Time) -> bool:
    """
        Checks if time_1 is after time_2
    """
    return time_1.hour*3600 + time_1.minute*60 + time_1.second > time_2.hour*3600 + time_2.minute*60 + time_2.second


def main() -> None:
    """
        The main function in the script
    """
    time_1 = Time()

    time_1.hour = 12
    time_1.minute = 59
    time_1.second = 32

    time_2 = Time()

    time_2.hour = 13
    time_2.minute = 59
    time_2.second = 32

    print(is_after(time_1, time_2))


if __name__ == "__main__":
    main()

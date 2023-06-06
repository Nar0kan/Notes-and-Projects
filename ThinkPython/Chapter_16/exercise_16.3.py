class Time(object):
    """
        Represents the time of day.
        attributes: hour, minute, second
    """


def increment(time: Time, seconds: int) -> None:
    """
        Increment time on certain amount of seconds
    """
    time.second += seconds

    if time.second >= 60:
        time.minute += time.second//60
        time.second = time.second%60

        if time.minute >= 60:
            time.hour += time.minute//60
            time.minute = time.minute%60

            if time.hour >= 24:
                time.hour = time.hour%24


def print_time(time: Time) -> str:
    """
        Prints the time in H:M:S format
    """
    time_format = '%.2d:%.2d:%.2d' % (time.hour, time.minute, time.second)
    print(time_format)
    return time_format


def main() -> None:
    """
        The main function in the script
    """
    time_1 = Time()

    time_1.hour = 12
    time_1.minute = 59
    time_1.second = 32

    increment(time_1, 200)
    print_time(time_1)


if __name__ == "__main__":
    main()

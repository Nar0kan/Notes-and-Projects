class Time(object):
    """
        Represents the time of day.
        attributes: hour, minute, second
    """


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
    time = Time()

    time.hour = 11
    time.minute = 59
    time.second = 30

    print_time(time)


if __name__ == "__main__":
    main()

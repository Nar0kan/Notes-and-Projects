from copy import deepcopy


class Time(object):
    """
        Represents the time of day.
        attributes: hour, minute, second
    """


def increment_pure(time: Time, seconds: int) -> None:
    """
        Increment time on certain amount of seconds and returns a new value
    """
    new_time = Time()
    new_time = deepcopy(time)

    new_time.second += seconds

    if new_time.second >= 60:
        new_time.minute += new_time.second//60
        new_time.second = new_time.second%60

        if new_time.minute >= 60:
            new_time.hour += new_time.minute//60
            new_time.minute = new_time.minute%60

            if new_time.hour >= 24:
                new_time.hour = new_time.hour%24

    return new_time


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

    new_time = increment_pure(time_1, 200)
    print_time(time_1)
    print_time(new_time)


if __name__ == "__main__":
    main()

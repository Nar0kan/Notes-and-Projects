from copy import deepcopy


class Time(object):
    """
        Represents the time of day.
        attributes: hour, minute, second
    """


def increment(time: Time, seconds: int) -> None:
    """
        Increment time on certain amount of seconds and returns a new value
    """
    return add_time(time, int_to_time(seconds))


def time_to_int(time: Time)-> int:
    """
        Converts the time to the integer (seconds)
    """
    return time.hour*3600 + time.minute*60 + time.second


def int_to_time(seconds: int) -> Time:
    """
        Converts integer (seconds) to the time format
    """
    time = Time()

    minutes, time.second = divmod(seconds, 60)
    hour, time.minute = divmod(minutes, 60)
    time.hour = hour%24

    return time


def add_time(t_1: Time, t_2: Time) -> Time:
    """
        Adds two times values and returns new time
    """
    seconds = time_to_int(t_1) + time_to_int(t_2)

    return int_to_time(seconds)


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

    time_2 = Time()

    time_2.hour = 7
    time_2.minute = 34
    time_2.second = 1

    new_time = increment(time_1, 3000)
    print_time(time_1)
    print_time(new_time)


if __name__ == "__main__":
    main()

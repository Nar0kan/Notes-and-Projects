from copy import deepcopy


class Time(object):
    """
        Represents the time of day.
        attributes: hour, minute, second
    """


def time_is_valid(time: Time) -> bool:
    return time.hour < 24 and time.minute < 60 and time.second < 60 \
        and isinstance(time.second, float) or isinstance(time.second, int)\
        and isinstance(time.hour, int) and isinstance(time.minute, int)


def increment(time: Time, seconds: int) -> None:
    """
        Increment time on certain amount of seconds and returns a new value
    """
    assert time_is_valid(time) and type(seconds) in (float, int)

    return add_time(time, int_to_time(seconds))


def time_to_int(time: Time)-> int:
    """
        Converts the time to the integer (seconds)
    """
    assert time_is_valid(time)
    return time.hour*3600 + time.minute*60 + time.second


def int_to_time(seconds: int) -> Time:
    """
        Converts integer (seconds) to the time format
    """
    assert type(seconds) in (float, int)

    time = Time()

    minutes, time.second = divmod(seconds, 60)
    hour, time.minute = divmod(minutes, 60)
    time.hour = hour%24

    return time


def add_time(t_1: Time, t_2: Time) -> Time:
    """
        Adds two times values and returns new time
    """
    assert time_is_valid(t_1) and time_is_valid(t_2)

    seconds = time_to_int(t_1) + time_to_int(t_2)

    return int_to_time(seconds)


def print_time(time: Time) -> str:
    """
        Prints the time in H:M:S format
    """
    assert time_is_valid(time)

    time_format = '%.2d:%.2d:%.2d' % (time.hour, time.minute, time.second)
    print(time_format)

    return time_format


def mul_time(time: Time, number: int) -> Time:
    """
        Multiplies the 'time' object, converting it to an integer
        with the 'number' and return new Time object after that
    """
    assert time_is_valid(time) and type(number) == int

    return int_to_time(time_to_int(time)*number)


def calculate_avarage_pace(time: Time, distance: int) -> Time:
    """
        Calculates avarage pace (time per mile) for finish time 'time'
        and 'distance' as an arguments and then return a new Time object
    """
    overal_time = time_to_int(time)
    return int_to_time(int(overal_time/distance))


def main() -> None:
    """
        The main function in the script
    """
    time_1 = Time()

    time_1.hour = 12
    time_1.minute = 59
    time_1.second = 32.6

    time_2 = Time()

    time_2.hour = 21
    time_2.minute = 34
    time_2.second = 5

    #print(time_is_valid(time_1), time_is_valid(time_2))
    print_time(time_1)
    new_time = mul_time(time_1, 3)
    print_time(new_time)
    print("Avarage pace (time per mile): ")
    print_time(calculate_avarage_pace(time_1, 25))


if __name__ == "__main__":
    main()

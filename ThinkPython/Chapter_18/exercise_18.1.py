from copy import deepcopy


class Time(object):
    """
        Represents the time of day.
        attributes: hour, minute, second
    """

    def __init__(self, hour: int=0, minute: int=0, second: int=0) -> None:
        self.hour, self.minute, self.second = hour, minute, second


    def __str__(self) -> str:
        """
            Prints the time in H:M:S format
        """
        return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)
    

    def __add__(self, other):
        if isinstance(other, Time):
            return int_to_time(self.time_to_int() + other.time_to_int())
        elif isinstance(other, int):
            return self.increment(other)
        else:
            raise ValueError("The parameter must be either integer or Time object!")


    def __radd__(self, other):
        return self.__add__(other)


    def __gt__(self, other):
        return self.time_to_int() > other.time_to_int()


    def __ge__(self, other):
        return self.time_to_int() >= other.time_to_int()


    def __lt__(self, other):
        return self.time_to_int() < other.time_to_int()


    def __le__(self, other):
        return self.time_to_int() <= other.time_to_int()


    def __eq__(self, other):
        return self.time_to_int() == other.time_to_int()


    def  __ne__(self, other):
        return self.time_to_int() != other.time_to_int()


    def increment(self, seconds: int) -> None:
        """
            Increment time on certain amount of seconds and returns a new value
        """
        seconds += self.time_to_int()

        return int_to_time(seconds)


    def time_to_int(self)-> int:
        """
            Converts the time to the integer (seconds)
        """
        return self.hour*3600 + self.minute*60 + self.second


    def is_after(self, other) -> bool:
        """
            Checks if the self time (first) is after the other one (seconds).
        """
        return self.time_to_int() > other.time_to_int()


def int_to_time(seconds: int) -> Time:
    """
        Converts integer (seconds) to the time format
    """
    time = Time()

    minutes, time.second = divmod(seconds, 60)
    hour, time.minute = divmod(minutes, 60)
    time.hour = hour%24

    return time


def main() -> None:
    """
        The main function in the script
    """
    time_1 = Time(12, 59)
    time_1.second = 32

    new_time = time_1.increment(200)

    print(time_1, " is coming after the ", new_time)
    print(time_1 > new_time)

    print(time_1, " is coming before the ", new_time)
    print(time_1 < new_time)

    print(time_1, " is coming after or is equal to ", time_1)
    print(time_1 >= time_1)

    print(time_1, " is coming before or is equal to ", new_time)
    print(time_1 <= new_time)

    print(time_1, " is equal to ", time_1)
    print(time_1 == time_1)

    print(time_1, " is equal to ", new_time)
    print(time_1 == new_time)

    print(time_1, " is not equal to ", time_1)
    print(time_1 != time_1)

    print(time_1, " is not equal to ", new_time)
    print(time_1 != new_time)


if __name__ == "__main__":
    main()

def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False
# Will correctly check each letter if it is lower
# And return False if any of them is upper-case
# True otherwise


def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'
# Will return True string on first iteration


def any_lowercase3(s):
    for c in s:
        flag = c.islower()
    return flag
# Return True if first character of s is lower
# else - False


def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag
# Will return True if the last character is lower case
# False - otherwise


def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True
# Will return False if first letter is not lower case
# True otherwise
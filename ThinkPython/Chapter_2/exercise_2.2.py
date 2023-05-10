# Data
width = 17
height = 12.0
delimiter = '.'


# Predict the value and its type

print(width/2)              # 8.5
print(type(width/2))        # float, default in python3
                            # in python2 result would be 8 and integer, because it is using floor()

print(width/2.0)            # 8.5
print(type(width/2.0))      # float, default in python3

print(height/3)             # 4.0
print(type(height/3))       # float, default in python3

print(1 + 2 * 5)            # 11
print(type(1 + 2 * 5))      # int, cause no division

print(delimiter*5)          # '.....'
print(type(delimiter*5))    # str, cause concatination
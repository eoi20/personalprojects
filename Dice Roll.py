import random

_value_ = str(input('Please input y if you want to roll the dice and n if you would not like to roll the dice'))

while _value_:
    if _value_ == 'y':
        _die_ = random.randrange(1, 7)
        print('You\'ve rolled:', _die_)
        _value_ = str(input('Would you like to roll again? Please input y if you want to roll the dice again and n if you would not like to roll the dice'))
    elif _value_ == 'n':
        print('You\'ve not rolled the die')
        break
    else:
        print('Input a valid instruction')
        break
     
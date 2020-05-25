import random
number = random.randrange(1, 11)
_inputnumber_ = int(input('Guess a number: '))
i=0
while _inputnumber_ >0:
    if _inputnumber_ > number:
        print("Inputed number is too high:")
        _inputnumber_ = int(input('Guess another number: '))
        i = i + 1
        
    elif _inputnumber_ < number:
        print("Inputed number is too low:")
        _inputnumber_ = int(input('Guess another number: '))
        i = i + 1
        
    else:
        print ('You have guessed the right number which is:', number)
        print ('You guessed {} times'.format(i))
        break
        
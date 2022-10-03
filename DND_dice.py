import random
def dice(type):
    type = type.upper()
    if type == 'D4':
        result = random.randrange(1,5)
    elif type == 'D6':
        result = random.randrange(1,7)
    elif type == 'D8':
        result = random.randrange(1,9)
    elif type == 'D10':
        result = random.randrange(1,11)
    elif type == 'D12':
        result = random.randrange(1,13)
    elif type == 'D20':
        result = random.randrange(1,21)
    else:
        return 'Invalid Dice, Please pick another '

    return result
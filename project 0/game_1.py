import numpy as np
number = np.random.randint(1,101)
count = 0
while True:
    count += 1
    predict_number = int(input('Guess a number from 1 to 100\n'))
    if predict_number > number:
        print('The number must be lesser')
    elif predict_number < number:
        print('The number must be greater')
    elif predict_number == number:
        print('You are right! This is the number')
        break
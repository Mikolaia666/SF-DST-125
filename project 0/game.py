import numpy as np
def random_predict(number:int=1) -> int:
    """Random number guessing
    Args: number(int, optional): the hidden number. Defaults to 1.
    Returns: int: number of attempts"""
    count = 0
    x = 1 #low bound of the interval
    y = 101 #high bound of the interval

    predict_number = np.random.randint(x, y)
    if number == predict_number: #guessed right on the first try
        count += 1
    else:
        while number != predict_number:
            count += 1
            if number < predict_number:
                x = number
                number = (x+y)//2
            elif number > predict_number:
                y = number
                number = (x+y)//2
            else:
                break
    return count

def score_game(random_predict) -> int:
    """Average number of attempts out of 1000
    approaches for wich the algorithm guesses
    Args:random_predict([type]): function for guessing
    Returns: int average nnumber of attempts"""
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=1000)
    for number in random_array:
        count_ls.append(random_predict(number)) #the list of the number of attempts
    score = int(np.mean(count_ls)) #the average value in the list of the number of attempts
    print(f'Average number of guesses: {score} attempts')
    return (score)

if __name__ == '__main__':
    score_game(random_predict)
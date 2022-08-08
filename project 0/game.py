import numpy as np
def random_predict(number:int=1) -> int:
    """Random number guessing
    Args: number(int, optional): the hidden number. Defaults to 1.
    Returns: int: number of attempts"""
    count = 0
    while True:
        count += 1
        predict_number = np.random.randint(1,101)
        if number == predict_number:
            break
    return(count)

def score_game(random_predict) -> int:
    """Average number of attempts out of 1000
    approaches for wich the algorithm guesses
    Args:random_predict([type]): function for guessing
    Returns: int average nnumber of attempts"""
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(random_predict(number))
    score = int(np.mean(count_ls))
    print(f'Average number of guesses: {score} attempts')
    return (score)

if __name__ == '__main__':
    score_game(random_predict)
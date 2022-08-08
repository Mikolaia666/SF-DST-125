import numpy as np
def random_predict(number:int=1) -> int:
    """Random number guessing
    Args: number(int, optional): the hidden number. Defaults to 1.
    Returns: int: number of attempts"""
    count = 0
    x = 1
    y = 100

    predict_number = np.random.randint(x, y)
    if number == predict_number:
        count += 1
    else:
        while number != predict_number:
            if number < predict_number:
                x = number
                number = np.random.randint(x, y)
                count += 1
            elif number > predict_number:
                y = number
                number = np.random.randint(x, y)
                count += 1
    return number
random_predict()
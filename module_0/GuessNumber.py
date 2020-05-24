import numpy as np


def play_game(number, max_number):
    if number > max_number:
        print(f'Загаданное число больше максимального. {number} > {max_number}')
        exit(1)

    try_count = 1
    min_predict = 0
    max_predict = max_number + 1
    predict = int(max_number / 2)

    while predict != number:
        # print(predict, min_predict, max_predict)
        if predict > number:
            max_predict = predict
        else:
            min_predict = predict
        predict = int((min_predict + max_predict) / 2)
        try_count += 1

    return try_count


def score_game(game):
    game_results = []
    round_count = 1000
    max_guess_number = 100
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    game_inputs = np.random.randint(1, max_guess_number, size=round_count)

    for game_input in game_inputs:
        game_results.append(game(game_input, max_guess_number))

    score = int(np.mean(game_results))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score


score_game(play_game)

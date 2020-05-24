import math
import random


def play_game(number, max_number=100):
    try_count = 1
    min_predict = 0
    max_predict = max_number + 1
    predict = int(max_number / 2)
    max_try_count = math.ceil(math.log(max_number, 2))
    #print(predict, min_predict, max_predict)
    while predict != number:
        if predict > number:
            max_predict = predict
        else:
            min_predict = predict
        predict = int((min_predict + max_predict) / 2)
        try_count += 1
        if try_count > max_try_count:
            print('Something went wrong while trying to guess number', number)
            exit(1)
        #print(predict, min_predict, max_predict)
    return try_count

#print(math.ceil(math.log(100, 2))+1)
#print('Try count:', play_game(2))
#exit(0)

def score_game(game):
    count_ls = []
    random_array = []
    random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    round_count = 1000
    max_guess_number = 100
    for i in range(1, round_count + 1):
        random_array.append(random.randint(1, max_guess_number))

    for number in random_array:
        count_ls.append(game(number, max_guess_number))

    score = int(sum(count_ls) / len(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score


score_game(play_game)


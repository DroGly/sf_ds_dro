import numpy as np
# Эта функция угадывает число. Отлично работает сама по себе.
def random_predict (number):
    min = 1
    max = 101
    count = 0
    while True:
        count+=1
        mid = round((min+max) / 2) #берём середину диапазона
        if (min+max)/ 2 == 1.5:
            mid = 1
        if mid > number:
            max = mid
        elif mid < number:
            min = mid
        else:
            print (f"Компьютер угадал число за {count} попыток. Это число {number}")
            break #конец игры выход из цикла
    return count


def score_game(random_predict) -> int:
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size= 1000)  # загадали список чисел
    for number in random_array:
        count_ls.append(random_predict(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")
    return score

if __name__ == '__main__':
    # RUN
    score_game(random_predict)
    

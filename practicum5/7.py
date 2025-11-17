# Ввод данных
N, K, M = map(int, input("Введите N, K, M через пробел: ").split())

# Вычисление расстояний в двух направлениях
distance_clockwise = (M - K) % N
distance_counterclockwise = (K - M) % N

# Минимальное расстояние
min_distance = min(distance_clockwise, distance_counterclockwise)

# Вывод результата
print("Наименьшее количество станций:", min_distance - 1)
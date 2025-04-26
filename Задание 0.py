import sys
import math
from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QDoubleValidator

def calculate_ball_motion(initial_height, time):
    """
    Рассчитывает движение свободно падающего шара.

    Args:
        initial_height: Начальная высота шара (в метрах).
        time: Время, на которое нужно рассчитать движение (в секундах).

    Returns:
        Словарь со следующими ключами:
            "time_to_impact": Время падения до касания земли (в секундах).
            "impact_velocity": Скорость в момент касания земли (в м/с).
            "current_height": Текущая высота шара в момент времени time (в метрах).
            "current_velocity": Текущая скорость шара в момент времени time (в м/с).
            "valid_time": True, если время 'time' меньше или равно времени падения, иначе False
    """

    g = 9.81

    time_to_impact = math.sqrt(2 * initial_height / g)

    impact_velocity = g * time_to_impact

    valid_time = time <= time_to_impact

    if valid_time:
      current_height = initial_height - 0.5 * g * time**2
      current_velocity = g * time
    else:
     
      current_height = 0.0
      current_velocity = impact_velocity

    return {
        "time_to_impact": time_to_impact,
        "impact_velocity": impact_velocity,
        "current_height": current_height,
        "current_velocity": current_velocity,
        "valid_time": valid_time
    }


# Получение входных данных от пользователя
try:
    initial_height = float(input("Начальная высота (в метрах): "))
    time = float(input("Время (в секундах): "))
except ValueError:
    print("Ошибка: Пожалуйста, введите числовые значения для высоты и времени.")
    exit()


# Расчет движения шара
results = calculate_ball_motion(initial_height, time)


# Вывод результатов
print("\n--- Результаты расчёта ---")
print(f"Время падения до касания земли: {results['time_to_impact']:.2f} сек")
print(f"Скорость в момент касания земли: {results['impact_velocity']:.2f} м/с")

if results['valid_time']:
    print(f"Текущая высота (в момент {time} сек): {results['current_height']:.2f} м")
    print(f"Текущая скорость (в момент {time} сек): {results['current_velocity']:.2f} м/с")
else:
    print(f"Шар уже достиг земли к моменту {time} сек.")
    print(f"Высота: {results['current_height']} м")
    print(f"Скорость: {results['current_velocity']:.2f} м/с") # Скорость равна скорости в момент касания земли.


print("-------------------------")
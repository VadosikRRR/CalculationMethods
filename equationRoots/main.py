import math
from RootsFinder import RootFinder


def ball_task(root_finder: RootFinder, density: float, radius: float):
    func = lambda x: math.pi * (x**3 - 3*radius*x**2 + 4*radius**3*density)
    return root_finder.solve_task(func, 10e-6, 0, 2*radius, 3)


if __name__ == "__main__":
    root_finder = RootFinder()
    root_finder.start()

    # key (, density) - value (answer)
    ball_data = {
        ("Пробка", 0.25): 0,
        ("Бамбук", 0.4): 0,
        ("Сосна (белая)", 0.5): 0,
        ("Кедр", 0.55): 0,
        ("Дуб", 0.7): 0,
        ("Бук", 0.75): 0,
        ("Красное дерево", 0.8): 0,
        ("Тиковое дерево", 0.85): 0,
        ("Парафин", 0.9): 0,
        ("Лёд/Полиэтилен", 0.92): 0,
        ("Пчелинный воск", 0.95): 0,
    }

    radius = float(input("Введите радиус: "))
    print("\n")
    for key in ball_data.keys():
        ball_data[key] = ball_task(root_finder, key[1], radius)
        print(f"Материал: {key[0]}, плотность: {key[1]}, глубина погружения: {ball_data[key]:.2f}\n")

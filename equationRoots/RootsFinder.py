from random import random
from sympy import symbols, diff, lambdify, sympify


class RootFinder:
    def __init__(self):
        self.big_value = 1000
        pass

    def start(self):
        self.input_data()
        result, delta, iter = self.solve_by_bisection()
        print(
            f"\nМетод Бисекции\nx = {result}\n"
            f"Длина конечного интервала = {delta}\n"
            f"Количество итераций = {iter}\n"
        )

        result, iter = self.solve_by_newtons_method()
        print(
            f"\nМетод Ньютона\nx = {result}\nКоличество итераций = {iter}\n"
        )

        result, iter = self.solve_by_modified_newtons_method()
        print(
            f"\nУсовершенствованный метод Ньютона\nx = {result}\nКоличество итераций = {iter}\n"
        )

        result, iter = self.solve_by_secant_method()
        print(
            f"\nМетод секущих\nx = {result}\nКоличество итераций = {iter}\n"
        )

    def input_data(self):
        self.input_func()
        self.eps = float(input("Введите Eps: "))
        self.interval = self.root_separation()

    def input_func(self):
        x = symbols('x')
        func_string = input("Введите формулу: ")
        f_sym = sympify(func_string)
        self.func = lambdify(x, f_sym, modules="math")
        first_func_diff = diff(f_sym, x)
        self.first_func_diff = lambdify(x, first_func_diff, 'math')

    def root_separation(self) -> tuple[float, float]:
        A, B, N = map(float, input("Введите A, B и N через пробел: ").split(" "))
        intervals = []
        h = (B-A) / N
        x1 = A
        x2 = A + h
        y1 = self.func(x1)
        while x2 <= B:
            y2 = self.func(x2)
            if y1*y2 <= 0:
                intervals.append((x1, x2))
            
            x1 = x2
            x2 = x1 + h
            y1 = y2

        print(
            f"После процедуры отделения корней на промежутке [{A}, {B}] при N = {int(N)} "
            "были найдены следующие промежутки, содержащие корень нечётной степени:"
        )

        for ind in range(len(intervals)):
            print(f"{ind + 1}: [{intervals[ind][0], intervals[ind][1]}]")

        choice = int(input(
            "Введите номер отрезка, на котором хотите найти корень или" 
            "введите -1, если хотите провести процедуру отделение корней заного.\n"
        ))
        
        return self.root_separation() if choice == -1 else intervals[choice - 1]

    def solve_by_bisection(self) -> tuple[float, float, int]:
        a = self.interval[0]
        b = self.interval[1]
        iter = 0
        while b - a > 2 * self.eps:
            iter += 1
            c = (a + b) / 2
            if self.func(a) * self.func(c) <= 0:
                b = c
            else:
                a = c
        
        return (a + b) / 2, (b - a) / 2, iter, 

    def solve_by_newtons_method(self):
        delta = 0
        while True:
            x_current = self.interval[0] + delta
            for iter in range(1, 1001):
                try:
                    div = self.first_func_diff(x_current)
                except:
                    div = self.big_value

                x_next = x_current - self.func(x_current) / div
                if abs(x_next - x_current) < self.eps:
                    return x_next, iter
                
                x_current = x_next
            
            delta = self.interval[1] - self.interval[0] * random()

    def solve_by_modified_newtons_method(self):
        delta = 0
        while True:
            x_current = self.interval[0] + delta
            try:
                div = self.first_func_diff(x_current)
            except:
                div = self.big_value
            
            for iter in range(1, 1001):
                x_next = x_current - self.func(x_current) / div
                if abs(x_next - x_current) < self.eps:
                    return x_next, iter
                
                x_current = x_next
            
            delta = self.interval[1] - self.interval[0] * random()

    def solve_by_secant_method(self):
        x1 = self.interval[0]
        x2 = self.interval[1]
        for iter in range(1, 1001):
            x3 = x2 - 1.618 * self.func(x2) / (self.func(x2) - self.func(x1))
            if abs(x3 - x2) < self.eps:
                return x3, iter
            
            x1 = x2
            x2 = x3

        raise(Exception("Baad, very baad"))

import matplotlib.pyplot as plt
import numpy as np

axiom = 'F--F--F'
rules = {'F': 'F+F--F+F'}
angle = 60


def koch_snowflake(txt, n):
    if n == 0:
        return txt
    new_txt = ''
    for char in txt:
        new_txt += rules.get(char, char)
    return koch_snowflake(new_txt, n - 1)


def draw(txt):
    direction = 0
    x, y = 0, 0
    stack = []
    line_segments = []

    for command in txt:
        if command == 'F':
            x_new = x + np.cos(np.radians(direction))
            y_new = y + np.sin(np.radians(direction))
            line_segments.append(((x, y), (x_new, y_new)))
            x, y = x_new, y_new
        elif command == '+':
            direction -= angle
        elif command == '-':
            direction += angle

    return line_segments


def plot_snowflake(segments):
    plt.figure(figsize=(8, 8))
    for ((x1, y1), (x2, y2)) in segments:
        plt.plot([x1, x2], [y1, y2], 'blue')
    plt.axis('equal')
    plt.axis('off')
    plt.show()





def main():
    """
    Основна функція для запуску програми.
    """
    order = int(input("Введіть рівень рекурсії для сніжинки Коха: "))
    txt = koch_snowflake(axiom, order)
    segments = draw(txt)
    plot_snowflake(segments)


if __name__ == "__main__":
    main()

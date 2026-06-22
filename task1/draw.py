#!/usr/bin/env python3

screen_size = (20, 20)
segments = [
    # (2, 1, 10, 1),
    # (15, 2, 15, 12),
    # (5, 5, 1, 11),
    # (10, 2, 2, 2),
    # (3, 3, 3, 3),
]

screen = []

def draw_line(segment, screen):
    x0 = segment[0]
    x1 = segment[2]
    y0 = segment[1]
    y1 = segment[3]
    for i in [segment[0], segment[2]]:
        if i < 0 or i >= screen_size[0]:
            raise Exception("Out of bounds x {i}")
    for i in [segment[1], segment[3]]:
        if i < 0 or i >= screen_size[1]:
            raise Exception("Out of bounds y {i}")
    dx = x1 - x0
    dy = y1 - y0
    md = max(abs(dx), abs(dy))
    step_y = float(dy) / md if md else 0
    step_x = float(dx) / md if md else 0
    x = x0
    y = y0
    for i in range(md):
        screen[round(y)][round(x)] = '.'
        x += step_x
        y += step_y
    screen[round(y1)][round(x1)] = '.'


def init():
    for _ in range(screen_size[0]):
        screen.append([" " for _ in range(screen_size[1])])

def draw_lines():
    for l in segments:
        draw_line(l, screen)

def draw():
    print("-" * (screen_size[1] + 2))
    for i in range(screen_size[0]):
        line = ''.join([c for c in screen[i]])
        print('|' + line + '|')
    print("-" * (screen_size[1] + 2))

def main():
    init()
    while True:
        line = input("Enter line segment (x0,y0,x1,y1): ")
        segment_str = line.split(",")
        segment = [int(i) for i in segment_str]
        print(f"You entered: {segment}")
        draw_line(segment, screen)
        draw()


if __name__ == "__main__":
    main()
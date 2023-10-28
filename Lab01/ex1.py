import pygame
import time
from pygame.locals import *

# Kích thước màn hình
WIDTH, HEIGHT = 640, 480
# Màu sắc
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

def draw_point(screen, x, y):
    pygame.draw.rect(screen, BLUE, (x, y, 1, 1))
    time.sleep(0.001)

def draw_line(screen, x1, y1, x2, y2):
    Dx = abs(x2 - x1)
    Dy = abs(y2 - y1)
    x = x1
    y = y1
    x_unit = 1 if x2 - x1 >= 0 else -1
    y_unit = 1 if y2 - y1 >= 0 else -1
    
    if x1 == x2: #thẳng đứng
        for y in range(y1, y2+y_unit, y_unit):
            draw_point(screen, x, y)
    elif y1 == y2: #đường ngang
        for x in range(x1, x2+x_unit, x_unit):
            draw_point(screen, x, y)
    else:
        draw_point(screen, x, y)
        if 1 >= Dy/Dx and Dy/Dx > 0:
            p = 2 * Dy - Dx
            for x in range(x1, x2+x_unit, x_unit):
                if p < 0:
                    p += 2 * Dy
                else:
                    p += 2 * (Dy - Dx)
                    y += y_unit
                draw_point(screen, x, y)
        else:
            p = 2 * Dx - Dy
            for y in range(y1, y2+y_unit, y_unit):
                if p < 0:
                    p += 2 * Dx
                else:
                    p += 2 * (Dx - Dy)
                    x += x_unit
                draw_point(screen, x, y)
            

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Bresenham Line Drawing")
    screen.fill(WHITE)

    drawing = False
    start_point = None

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == MOUSEBUTTONDOWN:
                if not drawing:
                    start_point = pygame.mouse.get_pos()
                    drawing = True
                else:
                    end_point = pygame.mouse.get_pos()
                    draw_line(screen, start_point[0], start_point[1], end_point[0], end_point[1])
                    pygame.display.flip()
                    drawing = False
    pygame.quit()

if __name__ == "__main__":
    main()

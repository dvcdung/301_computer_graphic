import pygame
from pygame.locals import *

# Kích thước màn hình
WIDTH, HEIGHT = 640, 480

# Màu sắc
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

def draw_4_points(screen, xc, yc, x, y, color):
    pygame.draw.rect(screen, color, (xc + x, yc + y, 1, 1))
    pygame.draw.rect(screen, color, (xc - x, yc + y, 1, 1))
    pygame.draw.rect(screen, color, (xc - x, yc - y, 1, 1))
    pygame.draw.rect(screen, color, (xc + x, yc - y, 1, 1))
    pygame.display.flip()

def draw_ellipse(screen, x_center, y_center, a, b, color):
    a2 = a**2
    b2 = b**2
    x = 0
    y = b
    p = 2 * (b2 / a2) - 2 * b + 1

    while (b2 / a2) * x <= y:
        draw_4_points(screen, x_center, y_center, x, y, color)
        if p < 0:
            p += 2 * (b2 / a2) * (2 * x + 3)
        else:
            p += 2 * (b2 / a2) * (2 * x + 3) - 4 * y
            y -= 1
        x += 1

    y = 0
    x = a
    p = 2 * (a2 / b2) - 2 * a + 1

    while (a2 / b2) * y <= x:
        draw_4_points(screen, x_center, y_center, x, y, color)
        if p < 0:
            p += 2 * (a2 / b2) * (2 * y + 3)
        else:
            p += 2 * (a2 / b2) * (2 * y + 3) - 4 * x
            x -= 1
        y += 1

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Ellipse Drawing")
    screen.fill(WHITE)

    drawing = False
    x_center, y_center = None, None
    a, b = None, None

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == MOUSEBUTTONDOWN:
                if not drawing:
                    x_center, y_center = pygame.mouse.get_pos()
                    drawing = True
                else:
                    end_point = pygame.mouse.get_pos()
                    a = abs(end_point[0] - x_center)
                    b = abs(end_point[1] - y_center)
                    draw_ellipse(screen, x_center, y_center, a, b, BLUE)
                    pygame.display.flip()
                    drawing = False

    pygame.quit()

if __name__ == "__main__":
    main()

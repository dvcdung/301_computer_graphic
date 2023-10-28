import pygame
import sys

pygame.init()

# Kích thước màn hình
WIDTH, HEIGHT = 640, 480
# Màu sắc
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(WHITE)
pygame.display.set_caption("Bresenham Circle Drawing")

def draw_circle(xc, yc, radius):
    x = 0
    y = radius
    p = 3 - 2 * radius

    def plot_points(xc, yc, x, y):
        pygame.draw.circle(screen, BLUE, (xc + x, yc + y), 1)
        pygame.draw.circle(screen, BLUE, (xc - x, yc + y), 1)
        pygame.draw.circle(screen, BLUE, (xc + x, yc - y), 1)
        pygame.draw.circle(screen, BLUE, (xc - x, yc - y), 1)
        pygame.draw.circle(screen, BLUE, (xc + y, yc + x), 1)
        pygame.draw.circle(screen, BLUE, (xc - y, yc + x), 1)
        pygame.draw.circle(screen, BLUE, (xc + y, yc - x), 1)
        pygame.draw.circle(screen, BLUE, (xc - y, yc - x), 1)

    plot_points(xc, yc, x, y)

    while x <= y:
        x += 1
        if p > 0:
            y -= 1
            p = p + 4 * (x - y) + 10
        else:
            p = p + 4 * x + 6
        plot_points(xc, yc, x, y)

drawing = False
center = None
radius = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if not drawing:
                center = event.pos
                drawing = True
            else:
                end_point = event.pos
                radius = int((abs(center[0] - end_point[0]) ** 2 + abs(center[1] - end_point[1]) ** 2) ** 0.5)
                drawing = False
                draw_circle(center[0], center[1], radius)
                center = None
                radius = 0
    pygame.display.flip()

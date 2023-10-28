import pygame
from pygame.locals import *

# Kích thước màn hình
WIDTH, HEIGHT = 640, 480
# Màu sắc
WHITE = (255, 255, 255, 255)
BLUE = (0, 0, 255, 255)
RED = (255, 0, 0, 255)

def draw_point(screen, x, y):
    pygame.draw.rect(screen, BLUE, (x, y, 1, 1))

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
                
def push_to_stack(screen, stack, x, y):
    colour = screen.get_at((x, y))
    if colour != BLUE and colour != RED:
        pygame.draw.rect(screen, RED, (x, y, 1, 1))
        stack.append((x, y))
        
def boundary_fill(screen, x, y):
    stack = []
    pygame.draw.rect(screen, RED, (x, y, 1, 1))
    stack.append((x, y))
    
    while stack:
        xi, yi = stack.pop()
        push_to_stack(screen, stack, xi+1, yi)
        push_to_stack(screen, stack, xi-1, yi)
        push_to_stack(screen, stack, xi, yi+1)
        push_to_stack(screen, stack, xi, yi-1)
    
# def boundary_fill(screen, x, y):
#     colour = screen.get_at((x, y))
#     if colour != BLUE and colour != RED:
#         pygame.draw.rect(screen, RED, (x, y, 1, 1))
#         boundary_fill(screen, x, y+1)
#         boundary_fill(screen, x+1, y)
#         boundary_fill(screen, x-1, y)
    
def draw_polygon(screen, points):
    verNum = len(points)
    for i in range(verNum):
        x1, y1 = points[i]
        if i < verNum - 1:
            x2, y2 = points[i+1]
        else:
            x2, y2 = points[0]
        draw_line(screen, x1, y1, x2, y2)

    boundary_fill(screen, 300, 60)
                
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Bresenham Line Drawing")
    screen.fill(WHITE)
    
    points = [(100, 100), (300, 50), (550, 350), (250, 180), (50, 200)]
    draw_polygon(screen, points)
    
    while True:
        for event in pygame.event.get() :
            if event.type == QUIT:
                pygame.quit()
                quit()
        pygame.display.flip()
    
if __name__ == "__main__":
    main()
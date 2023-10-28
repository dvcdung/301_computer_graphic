import pygame
from pygame.locals import *

# Kích thước màn hình
WIDTH, HEIGHT = 640, 480
# Màu sắc
WHITE = (255, 255, 255, 255)
BLUE = (0, 0, 255, 255)
RED = (255, 0, 0, 255)

points = [(100, 100), (300, 50), (380, 150), (280, 180), (380, 210), (250, 280), (150, 200)]
    
# Tìm giá trị y tối đa và y tối thiểu trong đa giác
min_x = min(point[0] for point in points)
max_x = max(point[0] for point in points)

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

def scanline_fill(screen):
    for x in range(min_x, max_x+1):
        # giao diem 
        intersections = []
        # print(points)
        for i in range(len(points)):
            xt, yt = points[(i-1+len(points))%len(points)]
            xi, yi = points[i]
            xs, ys = points[(i+1)%len(points)]
            # print(f"{xt},{yt} - {xi},{yi} - {xs},{ys}")
            
            if x == xi:
                if min(xt, xs) < x < max(xt, xs):
                    intersections.append(yi)
                else:
                    intersections.append(yi)
                    intersections.append(yi)
            elif x in range(xi+1, xs) or x in range(xs+1, xi):
                y = yi + (x-xi)*(ys-yi)/(xs-xi)
                intersections.append(y)
        intersections.sort()
        for i in range(0, len(intersections), 2):
            pygame.draw.line(screen, RED, (x, int(intersections[i])), (x, int(intersections[i+1])))
                
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Bresenham Line Drawing")
    screen.fill(WHITE)
    
    scanline_fill(screen)
    
    while True:
        for event in pygame.event.get() :
            if event.type == QUIT:
                pygame.quit()
                quit()
        pygame.display.flip()
    
if __name__ == "__main__":
    main()
import pygame
import sys

pygame.init()

window_width = 400
window_height = 400

white = (255, 255, 255)
black = (0, 0, 0)

screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Binary Division")
screen.fill(white)

x_min, y_min, x_max, y_max = 100, 100, 300, 300
border_color = (255, 0, 0)
x1, y1, x2, y2 = 0, 0, 0, 0

def inside_clip(point):
    if x_min <= point[0] <= x_max and y_min <= point[1] <= y_max:
        return 0
    return 1

def binary_clip(p1, p2):
    if (inside_clip(p1) | inside_clip(p2)) == 0:
        draw_line(p1, p2)
    if (inside_clip(p1) & inside_clip(p2)) != 0:
        return
    if (inside_clip(p1) != 0) and (inside_clip(p2) == 0):
        p1, p2 = p2, p1
    if (inside_clip(p1) == 0) and (inside_clip(p2) != 0):
        P, Q = p1, p2
        while (abs(P[0] - Q[0]) + abs(P[1] - Q[1])) > 2:
            M = ((P[0] + Q[0]) // 2, (P[1] + Q[1]) // 2)
            if inside_clip(M) == 0:
                P = M
            else:
                Q = M
        draw_line(p1, P)
    
    if ((inside_clip(p1) != 0) and (inside_clip(p2) != 0)) and ((inside_clip(p1) & inside_clip(p2)) == 0):
        P, Q = p1, p2
        while (inside_clip(M) != 0) and ((abs(P[0] - Q[0]) + abs(P[1] - Q[1])) > 2):
            M = ((P[0] + Q[0]) // 2, (P[1] + Q[1]) // 2)
            if (inside_clip(P) & inside_clip(M)) != 0:
                P = M
            else:
                Q = M
        if inside_clip(M) == 0:
            binary_clip(P, M)
            binary_clip(M, Q)

def draw_line(start, end):
    pygame.draw.line(screen, black, start, end)
    pygame.display.update()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if x1 == 0:
                x1, y1 = event.pos
            else:
                x2, y2 = event.pos
                binary_clip((x1, y1), (x2, y2))
                x1, y1, x2, y2 = 0, 0, 0, 0

    pygame.draw.rect(screen, border_color, (x_min, y_min, x_max - x_min, y_max - y_min), 1)

    pygame.display.update()

pygame.quit()
sys.exit()

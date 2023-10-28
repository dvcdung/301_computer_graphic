import pygame
import sys

pygame.init()

window_width = 400
window_height = 400

border_width = 5

white = (255, 255, 255)
blue = (0, 0, 255)
fill_color = (0, 0, 0)

screen = pygame.display.set_mode((window_width, window_height))
screen.fill(white)
pygame.display.set_caption("Cohen-Sutherland")

x_min, y_min, x_max, y_max = 100, 100, 300, 300
border_color = (255, 0, 0) 

x1, y1, x2, y2 = 0, 0, 0, 0

def compute_region_code(x, y):
    code = 0
    if x < x_min:
        code |= 1
    if x > x_max:
        code |= 2
    if y < y_min:
        code |= 4 
    if y > y_max:
        code |= 8 
    return code

def cohen_sutherland(x1, y1, x2, y2):
    code1 = compute_region_code(x1, y1)
    code2 = compute_region_code(x2, y2)

    while True:
        if code1 == 0 and code2 == 0:
            return [(x1, y1), (x2, y2)]
        elif code1 & code2 != 0:
            return None
        else:
            code = code1 if code1 != 0 else code2
            x, y = 0, 0

            if code & 1:
                x = x_min
                y = y1 + (y2 - y1) * (x_min - x1) / (x2 - x1)
            elif code & 2:
                x = x_max
                y = y1 + (y2 - y1) * (x_max - x1) / (x2 - x1)
            elif code & 4:
                y = y_min
                x = x1 + (x2 - x1) * (y_min - y1) / (y2 - y1)
            elif code & 8:
                y = y_max
                x = x1 + (x2 - x1) * (y_max - y1) / (y2 - y1)

            if code == code1:
                x1, y1 = x, y
                code1 = compute_region_code(x1, y1)
            else:
                x2, y2 = x, y
                code2 = compute_region_code(x2, y2)

def boundary_fill(x, y):
    current_color = screen.get_at((x, y))
    if current_color != blue and current_color != fill_color:
        screen.set_at((x, y), fill_color)
        boundary_fill(x + 1, y)
        boundary_fill(x - 1, y)
        boundary_fill(x, y + 1)
        boundary_fill(x, y - 1)

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
                clipped_line = cohen_sutherland(x1, y1, x2, y2)
                if clipped_line:
                    pygame.draw.line(screen, blue, clipped_line[0], clipped_line[1])
                x1, y1, x2, y2 = 0, 0, 0, 0
    pygame.draw.rect(screen, border_color, (x_min, y_min, x_max - x_min, y_max - y_min), 1) 
    pygame.display.update()

pygame.quit()
sys.exit()

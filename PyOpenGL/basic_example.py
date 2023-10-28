import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Khởi tạo Pygame
pygame.init()

# Kích thước cửa sổ
window_width = 800
window_height = 600

# Tạo cửa sổ đồ họa
pygame.display.set_mode((window_width, window_height), pygame.RESIZABLE)

# Vòng lặp chính
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Đặc tả vẽ đồ họa ở đây
    pygame.display.flip()
    pygame.time.wait(10)
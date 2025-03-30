import pygame

pygame.init()

WIDTH , HEIGHT = 800,600
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Drawing Tool")


WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255 , 0, 0)
GREEN = (0 , 255 , 0)
BLUE = (0 , 0 , 255)
current_color = BLACK


running = True
mode = "circle"

screen.fill(WHITE)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                mode = "circle"

            elif event.key == pygame.K_r:
                mode = "rect"

            elif event.key == pygame.K_e:
                mode = "eraser"

            elif event.key == pygame.K_1:
                current_color = RED
            elif event.key == pygame.K_2:
                current_color = GREEN
            elif event.key == pygame.K_3:
                current_color = BLUE

        if pygame.mouse.get_pressed()[0]:
            x , y =pygame.mouse.get_pos()
            if mode == "circle":
                pygame.draw.circle(screen , current_color,(x , y) , 10) 
            if mode == "rect":
                pygame.draw.rect(screen , current_color , (x,y , 20 , 20))
            if mode == "eraser":
                pygame.draw.circle(screen , WHITE , (x,y), 15)  

    pygame.display.flip()

pygame.quit()                
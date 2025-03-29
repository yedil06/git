import pygame


pygame.init()


screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Red Ball")


BALL_RADIUS = 24
ball_x = 400
ball_y = 300
MOVE_STEP = 20

running = True
while running:
    screen.fill((255,255,255))

    pygame.draw.circle(screen , (255,0,0), (ball_x,ball_y), BALL_RADIUS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running == False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and ball_y - BALL_RADIUS - MOVE_STEP >= 0 :
                ball_y -= MOVE_STEP

            elif event.key == pygame.K_DOWN and ball_y + BALL_RADIUS + MOVE_STEP <=600:
                ball_y += MOVE_STEP

            elif event.key == pygame.K_LEFT and ball_x - BALL_RADIUS - MOVE_STEP >=0:
                ball_x -= MOVE_STEP

            elif event.key == pygame.K_RIGHT and ball_x + BALL_RADIUS + MOVE_STEP <= 800:
                ball_x += MOVE_STEP

    pygame.display.flip()

pygame.quit()                


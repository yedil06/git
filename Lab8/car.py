import pygame
import random

pygame.init()

# Настройки экрана
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Trash")

# Загрузка изображений
coin_img = pygame.image.load(r"C:\Users\Edik\Downloads\barcelona.png")
bin_img = pygame.image.load(r"C:\Users\Edik\Downloads\trashbin.jpg")

# Масштабирование
coin_img = pygame.transform.scale(coin_img, (40, 40))
bin_img = pygame.transform.scale(bin_img, (50, 50))

WHITE = (255, 255, 255)


# Класс мусорного бака
class TrashBin:
    def __init__(self):
        self.x = 400
        self.y = 500
        self.speed = 7

    def move(self, direction):
        if direction == "LEFT" and self.x > 0:
            self.x -= self.speed
        if direction == "RIGHT" and self.x < WIDTH - 50:
            self.x += self.speed

    def draw(self):
        SCREEN.blit(bin_img, (self.x, self.y))


# Класс эмблем Барселоны
class Coin:
    def __init__(self):
        self.x = random.randint(50, WIDTH - 50)
        self.y = -40
        self.speed = 5

    def fall(self):
        self.y += self.speed

    def draw(self):
        SCREEN.blit(coin_img, (self.x, self.y))


# Функция проверки столкновений
def check_collision(trash_bin, falling_coin):
    return pygame.Rect(trash_bin.x, trash_bin.y, 50, 50).colliderect(
        pygame.Rect(falling_coin.x, falling_coin.y, 40, 40)
    )


# Основной игровой цикл
trash_bin = TrashBin()
coins = []
score = 0

running = True
clock = pygame.time.Clock()
while running:
    SCREEN.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        trash_bin.move("LEFT")
    if keys[pygame.K_RIGHT]:
        trash_bin.move("RIGHT")

    if random.randint(1, 50) == 1:
        coins.append(Coin())

    for coin in coins[:]:
        coin.fall()
        if check_collision(trash_bin, coin):
            coins.remove(coin)
            score += 1

        elif coin.y > HEIGHT:  
            coins.remove(coin)

    trash_bin.draw()
    for coin in coins:
        coin.draw()

    
    font = pygame.font.SysFont(None, 36)
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    SCREEN.blit(score_text, (WIDTH - 150, 10))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()

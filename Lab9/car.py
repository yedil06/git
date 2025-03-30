import pygame
import random

pygame.init()

# Настройки экрана
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer Game")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Загрузка изображений
coin_img = pygame.image.load(r"C:\Users\Edik\Downloads\coin.jpg")
enemy_img = pygame.image.load(r"C:\Users\Edik\Downloads\car.jpg")
player_img = pygame.image.load(r"C:\Users\Edik\Downloads\skyline.png")

# Масштабирование изображений
coin_img = pygame.transform.scale(coin_img, (40, 40))
enemy_img = pygame.transform.scale(enemy_img, (50, 50))
player_img = pygame.transform.scale(player_img, (50, 50))

class Player:
    """Класс игрока (машины)"""
    def __init__(self):
        self.x = WIDTH // 2
        self.y = HEIGHT - 80
        self.speed = 7
    
    def move(self, direction):
        """Движение игрока влево или вправо"""
        if direction == "LEFT" and self.x > 0:
            self.x -= self.speed
        if direction == "RIGHT" and self.x < WIDTH - 50:
            self.x += self.speed
    
    def draw(self):
        """Отображение игрока на экране"""
        SCREEN.blit(player_img, (self.x, self.y))

class Coin:
    """Класс монеты с разным весом"""
    def __init__(self):
        self.x = random.randint(50, WIDTH - 50)
        self.y = -40
        self.speed = 5
        self.value = random.randint(1, 3)  # Случайный вес монеты (1-3 очка)
    
    def fall(self):
        """Движение монеты вниз"""
        self.y += self.speed
    
    def draw(self):
        """Отображение монеты на экране"""
        SCREEN.blit(coin_img, (self.x, self.y))

class Enemy:
    """Класс противника"""
    def __init__(self):
        self.x = random.randint(50, WIDTH - 50)
        self.y = -60
        self.speed = 5
    
    def fall(self):
        """Движение противника вниз"""
        self.y += self.speed
    
    def draw(self):
        """Отображение противника на экране"""
        SCREEN.blit(enemy_img, (self.x, self.y))

def check_collision(player, coin):
    """Проверка столкновения игрока с монетой"""
    return pygame.Rect(player.x, player.y, 50, 50).colliderect(coin.x, coin.y, 40, 40)

def check_collision_enemy(player, enemy):
    """Проверка столкновения игрока с противником (проигрыш)"""
    return pygame.Rect(player.x, player.y, 50, 50).colliderect(enemy.x, enemy.y, 50, 50)

# Инициализация игры
player = Player()
coins = []
enemies = []
score = 0
enemy_speed_increase_threshold = 10  # Каждые 10 очков враги ускоряются

running = True
clock = pygame.time.Clock()
while running:
    SCREEN.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.move("LEFT")
    if keys[pygame.K_RIGHT]:
        player.move("RIGHT")
    
    # Генерация монет
    if random.randint(1, 50) == 1:
        coins.append(Coin())
    
    # Генерация врагов
    if random.randint(1, 100) == 1:
        enemies.append(Enemy())
    
    # Обновление монет
    for coin in coins[:]:
        coin.fall()
        if check_collision(player, coin):
            coins.remove(coin)
            score += coin.value  # Учитываем вес монеты
        elif coin.y > HEIGHT:
            coins.remove(coin)
    
    # Обновление врагов
    for enemy in enemies[:]:
        enemy.fall()
        if check_collision_enemy(player, enemy):
            running = False  # Игра окончена при столкновении
        elif enemy.y > HEIGHT:
            enemies.remove(enemy)
    
    # Увеличение скорости врагов при достижении порога очков
    if score >= enemy_speed_increase_threshold:
        for enemy in enemies:
            enemy.speed += 1
        enemy_speed_increase_threshold += 10  # Новый порог увеличения
    
    # Отображение объектов
    player.draw()
    for coin in coins:
        coin.draw()
    for enemy in enemies:
        enemy.draw()
    
    # Отображение счета
    font = pygame.font.SysFont(None, 36)
    score_text = font.render(f"Score: {score}", True, BLACK)
    SCREEN.blit(score_text, (WIDTH - 150, 10))
    
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
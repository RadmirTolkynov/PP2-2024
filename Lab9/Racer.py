import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Racer")

# Colors
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)

# Player properties
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 100
PLAYER_COLOR = YELLOW
PLAYER_SPEED = 5

# Enemy properties
ENEMY_WIDTH = 50
ENEMY_HEIGHT = 50
ENEMY_COLOR = RED
ENEMY_SPEED = 4

# Coin properties
COIN_RADIUS = 15
COIN_COLOR = (255, 200, 0)
COIN_SPAWN_RATE = 0.02  # Chance of spawning a coin per frame
COIN_WEIGHTS = [1, 2, 3]  # Different weights for coins

# Fonts
font = pygame.font.SysFont(None, 30)

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((PLAYER_WIDTH, PLAYER_HEIGHT))
        self.image.fill(PLAYER_COLOR)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT - 20
        self.speed_x = 0

    def update(self):
        self.speed_x = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.speed_x = -PLAYER_SPEED
        if keys[pygame.K_RIGHT]:
            self.speed_x = PLAYER_SPEED
        self.rect.x += self.speed_x
        # Keep player in screen bounds
        self.rect.x = max(0, min(self.rect.x, WIDTH - PLAYER_WIDTH))

# Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((ENEMY_WIDTH, ENEMY_HEIGHT))
        self.image.fill(ENEMY_COLOR)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, WIDTH - ENEMY_WIDTH)
        self.rect.y = random.randrange(-1000, -ENEMY_HEIGHT)  # Off-screen initially

    def update(self):
        self.rect.y += ENEMY_SPEED
        # Respawn the enemy if it goes off-screen
        if self.rect.top > HEIGHT:
            self.rect.x = random.randrange(0, WIDTH - ENEMY_WIDTH)
            self.rect.y = random.randrange(-1000, -ENEMY_HEIGHT)

# Coin class
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Randomly choose a weight for the coin
        self.weight = random.choice(COIN_WEIGHTS)
        self.image = pygame.Surface((COIN_RADIUS*2, COIN_RADIUS*2))
        self.image.fill(WHITE)
        pygame.draw.circle(self.image, COIN_COLOR, (COIN_RADIUS, COIN_RADIUS), COIN_RADIUS)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, WIDTH - COIN_RADIUS*2)
        self.rect.y = random.randrange(-1000, -COIN_RADIUS*2)  # Off-screen initially

    def update(self):
        self.rect.y += 5
        # Respawn the coin if it goes off-screen
        if self.rect.top > HEIGHT:
            self.rect.x = random.randrange(0, WIDTH - COIN_RADIUS*2)
            self.rect.y = random.randrange(-1000, -COIN_RADIUS*2)

# Group for all sprites
all_sprites = pygame.sprite.Group()
enemies_group = pygame.sprite.Group()
coins_group = pygame.sprite.Group()

# Create player
player = Player()
all_sprites.add(player)

# Main loop
running = True
score = 0
coin_counter = 0  # Counter for tracking the number of collected coins
clock = pygame.time.Clock()

# Function to display game over message
def show_game_over():
    game_over_text = font.render("GAME OVER", True, WHITE)
    SCREEN.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - game_over_text.get_height() // 2))
    pygame.display.flip()
    pygame.time.delay(2000)  # Delay for 2 seconds
    pygame.quit()
    quit()

# Game loop
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Spawn enemies randomly
    if random.random() < 0.01:
        enemy = Enemy()
        all_sprites.add(enemy)
        enemies_group.add(enemy)

    # Spawn coins randomly
    if random.random() < COIN_SPAWN_RATE:
        coin = Coin()
        all_sprites.add(coin)
        coins_group.add(coin)

    # Collision detection with coins
    hits = pygame.sprite.spritecollide(player, coins_group, True)
    for hit in hits:
        score += 1
        coin_counter += hit.weight
        # Increase enemy speed when the player earns N coins
        if coin_counter >= 10:
            ENEMY_SPEED += 1
            coin_counter = 0  # Reset coin counter

    # Collision detection with enemies
    hits = pygame.sprite.spritecollide(player, enemies_group, False)
    if hits:
        show_game_over()

    # Update
    all_sprites.update()

    # Draw
    SCREEN.fill((0, 0, 0))
    all_sprites.draw(SCREEN)

    # Display score
    score_text = font.render("Score: " + str(score), True, WHITE)
    SCREEN.blit(score_text, (WIDTH - score_text.get_width() - 10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

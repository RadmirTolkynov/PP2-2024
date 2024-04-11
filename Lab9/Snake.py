import pygame
import random

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CELL_SIZE = 20
FPS = 10

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Directions
UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

class SnakeGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()
        self.snake = [(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)]
        self.direction = RIGHT
        self.food = self.generate_food()
        self.food_timer = 0
        self.score = 0
        self.level = 1
        self.speed = FPS

    def generate_food(self):
        while True:
            x = random.randint(0, (SCREEN_WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
            y = random.randint(0, (SCREEN_HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
            if (x, y) not in self.snake:
                return x, y

    def draw_snake(self):
        for segment in self.snake:
            pygame.draw.rect(self.screen, GREEN, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))

    def draw_food(self):
        pygame.draw.rect(self.screen, RED, (self.food[0], self.food[1], CELL_SIZE, CELL_SIZE))

    def check_collision(self):
        head_x, head_y = self.snake[0]
        # Check if snake collides with the wall
        if head_x < 0 or head_x >= SCREEN_WIDTH or head_y < 0 or head_y >= SCREEN_HEIGHT:
            return True
        # Check if snake collides with itself
        if (head_x, head_y) in self.snake[1:]:
            return True
        return False

    def check_eat_food(self):
        if self.snake[0] == self.food:
            self.snake.append(self.snake[-1])
            self.food = self.generate_food()
            self.score += 1
            # Increase speed and level after certain score
            if self.score % 3 == 0:
                self.level += 1
                self.speed += 1

    def display_stats(self):
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {self.score}", True, WHITE)
        level_text = font.render(f"Level: {self.level}", True, WHITE)
        self.screen.blit(score_text, (10, 10))
        self.screen.blit(level_text, (10, 50))

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and self.direction != DOWN:
                        self.direction = UP
                    elif event.key == pygame.K_DOWN and self.direction != UP:
                        self.direction = DOWN
                    elif event.key == pygame.K_LEFT and self.direction != RIGHT:
                        self.direction = LEFT
                    elif event.key == pygame.K_RIGHT and self.direction != LEFT:
                        self.direction = RIGHT

            # Move the snake
            head_x, head_y = self.snake[0]
            if self.direction == UP:
                head_y -= CELL_SIZE
            elif self.direction == DOWN:
                head_y += CELL_SIZE
            elif self.direction == LEFT:
                head_x -= CELL_SIZE
            elif self.direction == RIGHT:
                head_x += CELL_SIZE

            # Insert new head position
            self.snake.insert(0, (head_x, head_y))
            # Check for collisions
            if self.check_collision():
                running = False
                print("Game Over!")
            else:
                self.check_eat_food()
                # Remove tail segment
                if len(self.snake) > self.score + 1:
                    self.snake.pop()

            # Clear screen
            self.screen.fill(BLUE)
            # Draw snake and food
            self.draw_snake()
            self.draw_food()
            # Display stats
            self.display_stats()
            # Update display
            pygame.display.flip()
            # Control the game speed
            self.clock.tick(self.speed)
            # Increment food timer
            self.food_timer += 1
            # Check if food timer exceeds threshold and generate new food
            if self.food_timer >= FPS * 10:  # Food disappears after 10 seconds
                self.food = self.generate_food()
                self.food_timer = 0

        pygame.quit()

# Run the game
if __name__ == "__main__":
    game = SnakeGame()
    game.run()

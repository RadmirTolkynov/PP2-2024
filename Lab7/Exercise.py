import pygame
import time
import math

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pygame Applications")

# Load Mickey image
mickey_image = pygame.image.load("mickey.jpeg")
mickey_image = pygame.transform.scale(mickey_image, (200, 200))
mickey_rect = mickey_image.get_rect(center=(screen_width // 2, screen_height // 2))

# Load background music
pygame.mixer.music.load("music.mp3")

# Set up clock for time synchronization
clock = pygame.time.Clock()

# Set up colors
white = (255, 255, 255)
red = (255, 0, 0)

# Set up ball variables
ball_radius = 25
ball_x = screen_width // 2
ball_y = screen_height // 2
ball_speed = 20

# Function to rotate an image around its center
def rotate(image, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    rotated_rect = rotated_image.get_rect(center=image.get_rect(center=(screen_width // 2, screen_height // 2)).center)
    return rotated_image, rotated_rect

# Main loop
running = True
music_playing = False
while running:
    screen.fill(white)

    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if music_playing:
                    pygame.mixer.music.pause()
                    music_playing = False
                else:
                    pygame.mixer.music.unpause()
                    music_playing = True

    # Draw clock (Mickey's hands)
    current_time = time.localtime()
    minute_angle = 6 * current_time.tm_min
    second_angle = 6 * current_time.tm_sec

    minute_hand, minute_rect = rotate(mickey_image, -minute_angle)
    second_hand, second_rect = rotate(mickey_image, -second_angle)

    screen.blit(minute_hand, minute_rect)
    screen.blit(second_hand, second_rect)

    # Move the ball
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and ball_y - ball_speed >= 0:
        ball_y -= ball_speed
    if keys[pygame.K_DOWN] and ball_y + ball_speed <= screen_height:
        ball_y += ball_speed
    if keys[pygame.K_LEFT] and ball_x - ball_speed >= 0:
        ball_x -= ball_speed
    if keys[pygame.K_RIGHT] and ball_x + ball_speed <= screen_width:
        ball_x += ball_speed

    # Draw the ball
    pygame.draw.circle(screen, red, (ball_x, ball_y), ball_radius)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()

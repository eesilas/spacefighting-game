import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Silicon Workshop Python course: Space Game")

# Load the images
spaceship_img = pygame.image.load("spaceship.png")
bullet_img = pygame.image.load("bullet.png")
rock_imgs = [
    pygame.image.load("rock1.png"),
    pygame.image.load("rock2.png"),
    pygame.image.load("rock3.png")
]
#
#
# Set up the game objects
spaceship_x = screen_width // 2
spaceship_y = screen_height - 150
bullet_x = -1
bullet_y = -1
rock_x = random.randint(0, screen_width)
rock_y = -100
rock_img = random.choice(rock_imgs)
rock_speed = random.randint(1, 5)

# Set up the game loop
clock = pygame.time.Clock()
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                spaceship_x -= 35
            elif event.key == pygame.K_RIGHT:
                spaceship_x += 35
            elif event.key == pygame.K_SPACE:
                if bullet_y < 0:
                    bullet_x = spaceship_x + 20                   
                    bullet_y = spaceship_y

    # Move the objects
    rock_y += rock_speed
    if rock_y > screen_height:
        rock_x = random.randint(0, screen_width)
        rock_y = -100
        rock_img = random.choice(rock_imgs)
        rock_speed = random.randint(1, 3)
    if bullet_y >= 0:
        bullet_y -= 5
        if bullet_y < 0:
            bullet_x = -1

    # Draw the objects
    screen.fill((0, 75, 75))
    screen.blit(spaceship_img, (spaceship_x, spaceship_y))
    if bullet_y >= 0:
        screen.blit(bullet_img, (bullet_x, bullet_y))
    screen.blit(rock_img, (rock_x, rock_y))

    # Check for collisions
    if bullet_y >= 0 and rock_y >= 0:
        bullet_rect = pygame.Rect(bullet_x, bullet_y, 10, 20)
        rock_rect = pygame.Rect(rock_x, rock_y, 50, 50)
        if bullet_rect.colliderect(rock_rect):
            rock_x = random.randint(0, screen_width)
            rock_y = -100
            rock_img = random.choice(rock_imgs)
            rock_speed = random.randint(1, 3)
            bullet_x = -1
            bullet_y = -1

    # Update the display
    pygame.display.update()

    # Limit the frame rate
    clock.tick(60)

# Clean up
pygame.quit()
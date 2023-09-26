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
bullet_x1 = -1
bullet_x2 = -1   # add new
bullet_y1 = -1
bullet_y2 = -1    #add new 
rock_x1 = random.randint(0, screen_width)        # x to x1
rock_y1 = -100
rock_img1 = random.choice(rock_imgs)             # rock_img to rock_img1
rock_speed1 = random.randint(1, 5)               # rock_speed to rock_speed1

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
                spaceship_x -= 22
            elif event.key == pygame.K_RIGHT:
                spaceship_x += 22
            elif event.key == pygame.K_SPACE:
                if bullet_y1 < 0:
                    bullet_x1 = spaceship_x      # original spaceship_x + 20             
                    bullet_y1 = spaceship_y
                if bullet_y2 < 0:                #add new
                    bullet_x2 = spaceship_x + 38
                    bullet_y2 = spaceship_y
    # Move the objects
    rock_y1 += rock_speed1
    if rock_y1 > screen_height:
        rock_x1 = random.randint(0, screen_width)
        rock_y1 = -100
        rock_img1 = random.choice(rock_imgs)
        rock_speed1 = random.randint(1, 3)
    if bullet_y1 >= 0:           # y change to y1
        bullet_y1 -= 5
        if bullet_y1 < 0:
            bullet_x1 = -1
    if bullet_y2 >= 0:           # add four line here and below
        bullet_y2 -= 5
        if bullet_y2 < 0:
            bullet_x2 = -1

    # Draw the objects
    screen.fill((0, 75, 75))
    screen.blit(spaceship_img, (spaceship_x, spaceship_y))
    if bullet_y1 >= 0:                                              # y to y1
        screen.blit(bullet_img, (bullet_x1, bullet_y1))
    if bullet_y2 >= 0:
        screen.blit(bullet_img, (bullet_x2, bullet_y2))
    screen.blit(rock_img1, (rock_x1, rock_y1))

    # Check for collisions
    if bullet_y1 >= 0 and rock_y1 >= 0:               # add bullet_y2 condition
        bullet_rect = pygame.Rect(bullet_x1, bullet_y1, 10, 20)
        rock_rect = pygame.Rect(rock_x1, rock_y1, 50, 50)
        if bullet_rect.colliderect(rock_rect):
            rock_x1 = random.randint(0, screen_width)
            rock_y1 = -100
            rock_img1 = random.choice(rock_imgs)
            rock_speed1 = random.randint(1, 3)
            bullet_x1 = -1        # x to x1 y to y1  add two line x2 and y2
            bullet_y1 = -1
                
    if bullet_y2 >=0 and rock_y1 >= 0:               # add bullet_y2 condition
        bullet_rect = pygame.Rect(bullet_x2, bullet_y2, 10, 20)
        rock_rect = pygame.Rect(rock_x1, rock_y1, 50, 50)
        if bullet_rect.colliderect(rock_rect):
            rock_x1 = random.randint(0, screen_width)
            rock_y1 = -100
            rock_img1 = random.choice(rock_imgs)
            rock_speed1 = random.randint(1, 3)
            bullet_x2 = -1
            bullet_y2 = -1
            
    # Update the display
    pygame.display.update()

    # Limit the frame rate
    clock.tick(60)

# Clean up
pygame.quit()

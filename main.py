import pygame

from projectile import Projectile
from player import Player
from shield import ShieldGenerator

pygame.init()

# Create a clock object to track time
clock = pygame.time.Clock()

screen = pygame.display.set_mode((1280, 720))
# Set the title
pygame.display.set_caption('Space Invaders')

bg = pygame.image.load("bg.jpg")

# Entities creation
player = Player()
shields = ShieldGenerator().generate_shields(3)

exit_game = False
while not exit_game:

    # Quit the game if the user click the close button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True

    # Player actions on keypresses detection
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_q]:
        player.move_left()
    if keys_pressed[pygame.K_d]:
        player.move_right()
    if keys_pressed[pygame.K_SPACE]:
        player.shoot()

    # -------------------- DISPLAY UPDATE --------------------
    screen.blit(bg, (0, 0))

    for projectile in player.projectiles:
        projectile.move()
        projectile.draw(screen)

    for shield in shields:
        shield.draw(screen)

    player.draw(screen)

    # Update the display to the screen
    pygame.display.update()
    # Set framerate limit to 60
    clock.tick(60)

pygame.quit()

import pygame

from player import Player

pygame.init()

# Create a clock object to track time
clock = pygame.time.Clock()

screen = pygame.display.set_mode((1280, 720))
# Set the title
pygame.display.set_caption('Space Invaders')

bg = pygame.image.load("bg.jpg")

player = Player()

exit_game = False
while not exit_game:

    # Quit the game if the user click the close button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True

    # movements with keypresses detection
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_q]:
        player.move_left()
    if keys_pressed[pygame.K_d]:
        player.move_right()

    # -------------------- DISPLAY UPDATE --------------------
    screen.blit(bg, (0, 0))
    player.draw(screen)

    # Update the display to the screen
    pygame.display.update()
    # Set framerate limit to 60
    clock.tick(60)

pygame.quit()
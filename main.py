import pygame

from alien import Alien
from player import Player
from shield import ShieldGenerator
from sound import Sound

from config import ALIENS, SCREEN

pygame.init()

# Create a clock object to track time
clock = pygame.time.Clock()

screen = pygame.display.set_mode((SCREEN.get("width"), SCREEN.get("height")))
# Set the title
pygame.display.set_caption("Space Invaders")

bg = pygame.image.load("bg.jpg")




sound = Sound()


# Create a container for our explosions Sprites objects
explosions_grp = pygame.sprite.Group()

# -------------------- ALIENS --------------------
# Store the class attribute entities_list in var aliens
aliens = Alien.entities_list
# Create a container for our aliens Sprites objects
aliens_grp = pygame.sprite.Group()
# Generate all Aliens objects with configured x, y locations
for loc_x in ALIENS.get("x_locs"):
    for loc_y in ALIENS.get("y_locs"):
        # Create a new Alien Sprite
        alien = Alien(loc_x, loc_y, sound)
        # Add the Sprite to the Group
        aliens_grp.add(alien)



# Entities creation
player = Player(explosions_grp, sound)
shields = ShieldGenerator().generate_shields()

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

    # Draws the explosions Sprites contained in the group to the screen
    explosions_grp.draw(screen)
    # Calls the update method on contained Sprites to load the next image
    explosions_grp.update()

    for alien in aliens:
        alien.move()

    # Draws the aliens Sprites contained in the group to the screen
    aliens_grp.draw(screen)

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

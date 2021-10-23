import pygame

from alien import Alien
from config import SCREEN
from explosion import Explosion
from player import Player
from shield import ShieldGenerator
from sound import Sound

pygame.init()

# Create a clock object to track time
clock = pygame.time.Clock()

screen = pygame.display.set_mode((SCREEN.get("width"), SCREEN.get("height")))
# Set the title
pygame.display.set_caption("Space Invaders")

bg = pygame.image.load("bg.jpg")

# Create a container for our explosions Sprite objects
explosions_grp = pygame.sprite.Group()

# TEST ALIEN
aliens = []
aliens_grp = pygame.sprite.Group()
alien_locs = list(range(50, 1000, 100))
for loc in alien_locs:
    alien = Alien(loc, 50)
    # Add the Sprite to the Group
    aliens_grp.add(alien)
    aliens.append(alien)

sound = Sound()

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

    # Draws the contained Sprites to the screen
    explosions_grp.draw(screen)
    # Calls the update method on contained Sprites to load the next image
    explosions_grp.update()

    for alien in aliens:
        alien.move()

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

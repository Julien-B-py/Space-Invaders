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

myfont = pygame.font.SysFont('Comic Sans MS', 60)
text_surface = myfont.render('YOU WIN!', True, (255, 255, 255))

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
        alien = Alien(loc_x, loc_y, sound, aliens_grp, explosions_grp)
        # Add the Sprite to the Group
        aliens_grp.add(alien)

# Entities creation
player = Player(explosions_grp, sound, aliens)
shields = ShieldGenerator().generate_shields()

player_wins = False
exit_game = False
while not exit_game:

    print(player.health_points)

    # -------------------- USER INPUTS --------------------
    # Quit the game if the user click the close button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True

    if not player_wins:

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

        if not aliens:
            player_wins = True

        for alien in aliens:
            alien.move()
            alien.shoot()

        for alien in aliens:
            if alien.is_hitting_a_wall():
                Alien.velocity = -Alien.velocity
                Alien.move_down_required = True
                break

        if Alien.move_down_required:
            for alien in aliens:
                alien.move_down()
            Alien.move_down_required = False

        # Draws the aliens Sprites contained in the group to the screen
        aliens_grp.draw(screen)

        for projectile in player.projectiles:
            projectile.move()
            projectile.draw(screen)

        for alien in aliens:
            for projectile in alien.projectiles:

                if player.rect.x <= projectile.rect.x <= player.rect.x + player.rect.width:
                    if player.rect.y <= projectile.rect.y <= player.rect.y + player.rect.height:
                        projectile.explode()
                        projectile.delete()
                        player.take_damage()

                projectile.move()
                projectile.draw(screen)

        for shield in shields:
            shield.draw(screen)

        player.draw(screen)

    else:

        screen.blit(text_surface, ((SCREEN.get('width') - text_surface.get_width()) / 2,
                                   (SCREEN.get('height') - text_surface.get_height()) / 2))

    # Update the display to the screen
    pygame.display.update()
    # Set framerate limit to 60
    clock.tick(60)

pygame.quit()

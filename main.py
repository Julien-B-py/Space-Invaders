import pygame

from alien import Alien
from game import Game
from player import Player
from shield import ShieldGenerator
from sound import Sound

from config import ALIENS, SCREEN

pygame.init()

# Create a clock object to track time
clock = pygame.time.Clock()
# Set game window dimensions
screen = pygame.display.set_mode((SCREEN.get("width"), SCREEN.get("height")))
# Set the title
pygame.display.set_caption("Space Invaders")

game = Game()
sound = Sound()

# Create a container for our explosions Sprites objects
explosions_grp = pygame.sprite.Group()

# -------------------- ALIENS --------------------
# Store the class attribute entities_list in var aliens
aliens = Alien.entities_list
# Create a container for our aliens Sprites objects
aliens_grp = pygame.sprite.Group()
# Generate all Aliens objects with configured x, y locations
for loc_x in ALIENS.get("x_locations"):
    for loc_y in ALIENS.get("y_locations"):
        # Create a new Alien Sprite
        alien = Alien(loc_x, loc_y, sound, aliens_grp, explosions_grp, game)
        # Add the Sprite to the Group
        aliens_grp.add(alien)

# Entities creation
player = Player(explosions_grp, sound, aliens)
shields = ShieldGenerator().generate_shields()

# -------------------- GAME MAIN LOOP --------------------
while not game.exit:

    # -------------------- USER INPUTS --------------------
    # Quit the game if the user click the close button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.exit = True

    # If game is not over (there still are enemies or player still has health points)
    if not game.is_over:

        # Player actions on keypresses detection
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_q]:
            player.move_left()
        if keys_pressed[pygame.K_d]:
            player.move_right()
        if keys_pressed[pygame.K_SPACE]:
            player.shoot()

        # -------------------- DISPLAY UPDATE --------------------
        screen.blit(game.background, (0, 0))

        # Draws the explosions Sprites contained in the group to the screen
        explosions_grp.draw(screen)
        # Calls the update method on contained Sprites to load the next image
        explosions_grp.update()

        if not aliens or player.health_points == 0:
            game.is_over = True

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

                if (
                        player.rect.x
                        <= projectile.rect.x
                        <= player.rect.x + player.rect.width
                        and player.rect.y
                        <= projectile.rect.y
                        <= player.rect.y + player.rect.height
                ):
                    projectile.explode()
                    projectile.delete()
                    player.take_damage()

                projectile.move()
                projectile.draw(screen)

        for shield in shields:
            shield.draw(screen)

        player.draw(screen)

        game.display_player_hp(screen, player.health_points)
        game.display_player_score(screen)

    # If game over (there are no enemy left or player has no more health points)
    else:

        game.display_end_game_message(screen, player.health_points)

    # Update the display to the screen
    pygame.display.update()
    # Set framerate limit to 60
    clock.tick(60)

pygame.quit()

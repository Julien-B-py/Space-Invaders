import random

import pygame.sprite

from config import ALIENS
from projectile import Projectile


class Alien(pygame.sprite.Sprite):
    entities_list = []
    changed_direction = False
    dir_change_cpt = 0

    velocity = 1
    move_down_required = False

    def __init__(self, x: int, y: int, sound,
                 aliens_grp: pygame.sprite.Group, explosions_grp: pygame.sprite.Group, game):

        super().__init__()
        self.sound = sound
        self.image = pygame.image.load("img/sprites/alien.png")
        self.image = pygame.transform.scale(self.image, (self.image.get_width() // 4, self.image.get_height() // 4))

        # Define the amount of points the player will earn when destroying this alien ship
        self.points_value = random.choice([10, 20, 30])

        # -------------------- SPRITE COLORATION --------------------
        # Generate an image filled with a solid color having the same size as the Sprite:
        colouredImage = pygame.Surface(self.image.get_size())
        # Fill the image with a color depending on the random points value determined above
        colouredImage.fill(ALIENS.get('colors').get(self.points_value))
        # Draw the colored image onto the Sprite and use special_flags to specify the blending mode (similar to PS)
        self.image.blit(colouredImage, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
        # -----------------------------------------------------------
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.aliens_grp = aliens_grp
        self.explosions_grp = explosions_grp
        self.game = game

        self.projectiles = []
        # Everytime we create an Alien we add it to the class variable entities_list
        Alien.entities_list.append(self)

    def move(self) -> None:
        """
        Increment the x coordinate of the alien sprite rectangle by a specified amount to make it move left or right.
        """
        self.rect.x += Alien.velocity

    def move_down(self) -> None:
        """
        Increment the y coordinate of the alien sprite rectangle by a specified amount to make it move down.
        """
        self.rect.y += 25

    def is_hitting_a_wall(self) -> bool:
        return self.rect.x >= 1280 - self.rect.width or self.rect.x <= 0

    def destroy(self) -> None:
        """
        Removes the current alien Sprite object from the entities list and from the Sprite Group so it is no longer
        displayed.
        Increments player score by a set amount of points based on alien color.
        """
        Alien.entities_list.remove(self)
        self.aliens_grp.remove(self)
        self.game.increment_score(self.points_value)

    def shoot(self) -> None:
        """
        Generate a random number at each global game loop tour.
        If the random number is equal to the specified value and the alien have not shot a projectile yet we allow it to
        shoot a projectile.
        """
        # Use random to avoid getting all aliens shooting at the same time
        shoot_var = random.randint(1, 1500)
        # Make sure the alien doesn't have a current projectile on the screen (avoid burst)
        if shoot_var == 1500 and not self.projectiles:
            # Create a new projectile object
            self.projectiles.append(Projectile(owner=self, x=self.rect.x, y=self.rect.y, vel=-8))
            self.sound.play("shoot")

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

    def __init__(self, x, y, sound, aliens_grp, explosions_grp, game):
        super().__init__()
        self.sound = sound
        self.image = pygame.image.load("img/sprites/alien.png")
        self.image = pygame.transform.scale(self.image, (self.image.get_width() // 4, self.image.get_height() // 4))

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

        Alien.entities_list.append(self)

    def move(self):
        self.rect.x += Alien.velocity

    def move_down(self):
        self.rect.y += 25

    def is_hitting_a_wall(self):
        return self.rect.x >= 1280 - self.rect.width or self.rect.x <= 0

    def destroy(self):
        Alien.entities_list.remove(self)
        self.aliens_grp.remove(self)
        self.game.increment_score(self.points_value)

    def shoot(self):
        shoot_var = random.randint(1, 1500)
        if shoot_var == 1500 and not self.projectiles:
            self.projectiles.append(Projectile(owner=self, x=self.rect.x, y=self.rect.y, vel=-8))
            self.sound.play("shoot")

import pygame

from config import SCREEN
from projectile import Projectile


class Player:
    def __init__(self,explosions_grp, sound):
        self.image = pygame.image.load("player.png")
        self.image = pygame.transform.scale(self.image, (self.image.get_width() // 4, self.image.get_height() // 4))
        self.x = (SCREEN.get("width") - self.image.get_width()) // 2
        self.y = SCREEN.get("height") - self.image.get_height() - 10
        self.health_points = 3
        self.projectiles = []

        self.explosions_grp = explosions_grp
        self.sound = sound

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

    def move_left(self):
        if self.x <= 0:
            return
        self.x -= 5

    def move_right(self):
        if self.x >= SCREEN.get("width") - self.image.get_width():
            return
        self.x += 5

    def shoot(self):
        if not self.projectiles:
            self.projectiles.append(Projectile(self))
            self.sound.play('shoot')

# 4* 11 enemies
# 3 lives
# Score


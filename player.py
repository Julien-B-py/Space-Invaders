import pygame

from config import SCREEN
from projectile import Projectile


class Player:
    def __init__(self, explosions_grp, sound, aliens):
        self.image = pygame.image.load("player.png")
        self.image = pygame.transform.scale(self.image, (self.image.get_width() // 4, self.image.get_height() // 4))
        self.rect = self.image.get_rect()
        self.rect.x = (SCREEN.get("width") - self.image.get_width()) // 2
        self.rect.y = SCREEN.get("height") - self.image.get_height() - 10
        self.health_points = 3
        self.projectiles = []

        self.explosions_grp = explosions_grp
        self.sound = sound
        self.aliens = aliens

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))

    def move_left(self):
        if self.rect.x <= 0:
            return
        self.rect.x -= 5

    def move_right(self):
        if self.rect.x >= SCREEN.get("width") - self.image.get_width():
            return
        self.rect.x += 5

    def shoot(self):
        if not self.projectiles:
            self.projectiles.append(Projectile(owner=self, x=self.rect.x, y=self.rect.y, vel=8))
            self.sound.play('shoot')



    def take_damage(self):
        self.health_points -=1


# 3 lives
# Score

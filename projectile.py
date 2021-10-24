import pygame

from config import SCREEN
from explosion import Explosion


class Projectile:
    def __init__(self, player):
        self.image = pygame.image.load("ammo.png")
        self.image = pygame.transform.scale(self.image, (self.image.get_width() // 4, self.image.get_height() // 4))

        self.rect = self.image.get_rect()

        self.rect.x = player.x + 30
        self.rect.y = SCREEN.get("height") - self.image.get_height() - 20
        self.player = player

        self.velocity = 8
        # self.velocity = 40 # FOR TESTING

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))

    def move(self):

        for alien in self.player.aliens:
            if alien.rect.colliderect(self.rect):
                self.delete()
                self.explode()
                alien.destroy()

        if self.rect.y <= 0 - self.image.get_height():
            self.delete()

        self.rect.y -= self.velocity

    def delete(self):
        self.player.projectiles.remove(self)

    def explode(self):
        # TEST SPRITES
        # Create a Sprite object centered on x,y position
        explosion = Explosion(self.rect.x, self.rect.y)
        # Add the Sprite to the Group
        self.player.explosions_grp.add(explosion)
        self.player.sound.play('explosion')

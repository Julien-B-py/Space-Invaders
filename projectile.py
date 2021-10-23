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

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))

    def move(self):

        for alien in self.player.aliens:
            if alien.rect.colliderect(self.rect):
                self.delete()
                self.explode()



        if self.rect.y <= 0 - self.image.get_height():
            self.delete()
            self.explode()




        self.rect.y -= 8

    def delete(self):
        self.player.projectiles.remove(self)

    def explode(self):
        # TEST SPRITES
        # Create a Sprite object centered on x,y position
        explosion = Explosion(self.rect.x, self.rect.y)
        # Add the Sprite to the Group
        self.player.explosions_grp.add(explosion)
        self.player.sound.play('explosion')

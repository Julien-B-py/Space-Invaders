import pygame

import alien

from config import SCREEN
from explosion import Explosion


class Projectile:
    def __init__(self, owner, x, y, vel):
        self.image = pygame.image.load("ammo.png")
        self.image = pygame.transform.scale(self.image, (self.image.get_width() // 4, self.image.get_height() // 4))

        self.rect = self.image.get_rect()

        self.rect.center = (x + 30, y)

        self.owner = owner

        self.velocity = vel
        # self.velocity = 40 # FOR TESTING

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))

    def move(self):

        # If the bullet has been shot by an alien
        if isinstance(self.owner, alien.Alien):
            # If the bullet is out of the screen
            if self.rect.y >= SCREEN.get('height'):
                self.delete()

        # If player shot a bullet
        else:
            for _alien in self.owner.aliens:
                if _alien.rect.colliderect(self.rect):
                    self.delete()
                    self.explode()
                    _alien.destroy()

            if self.rect.y <= 0 - self.image.get_height():
                self.delete()

        # Decrement the bullet y coordinate by the defined amount of pixels in velocity variable.
        self.rect.y -= self.velocity

    def delete(self):
        self.owner.projectiles.remove(self)

    def explode(self):
        # TEST SPRITES
        # Create a Sprite object centered on x,y position
        explosion = Explosion(self.rect.x, self.rect.y)
        # Add the Sprite to the Group
        self.owner.explosions_grp.add(explosion)
        self.owner.sound.play('explosion')

import pygame

import alien

from config import SCREEN
from explosion import Explosion


class Projectile:
    def __init__(self, owner, x: int, y: int, vel: int):

        self.velocity = vel

        self.image = pygame.image.load("img/sprites/ammo.png")
        self.image = pygame.transform.scale(self.image, (self.image.get_width() // 4, self.image.get_height() // 4))

        # Rotates the projectile image if an alien ship is shooting it
        if self.velocity < 0:
            self.image = pygame.transform.rotate(self.image, 180)

        self.rect = self.image.get_rect()

        self.rect.center = (x + 30, y)

        self.owner = owner

        # self.velocity = 40 # FOR TESTING

    def draw(self, surface: pygame.Surface) -> None:
        """
        Draw the projectile on the game screen surface.
        """
        surface.blit(self.image, (self.rect.x, self.rect.y))

    def move(self) -> None:
        """
        Moves the projectile upwards or downwards depending of the entity that created it.
        """

        # If the bullet has been shot by an alien
        if isinstance(self.owner, alien.Alien):

            # If the bullet is out of the screen
            if self.rect.y >= SCREEN.get("height"):
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

    def delete(self) -> None:
        """
        Removes the projectile from his owner list to make it disappear from the screen.
        """
        self.owner.projectiles.remove(self)

    def explode(self) -> None:
        """
        Creates an Explosion Sprite object to display an animated explosion on the game screen when a projectile
        collides with a ship
        """
        # TEST SPRITES
        # Create a Sprite object centered on x,y position
        explosion = Explosion(self.rect.x, self.rect.y)
        # Add the Sprite to the Group
        self.owner.explosions_grp.add(explosion)
        self.owner.sound.play("explosion")

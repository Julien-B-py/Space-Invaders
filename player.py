import pygame

from config import SCREEN
from projectile import Projectile


class Player:
    def __init__(self, explosions_grp: pygame.sprite.Group, sound, aliens):

        self.image = pygame.image.load("img/sprites/player.png")
        self.image = pygame.transform.scale(self.image, (self.image.get_width() // 4, self.image.get_height() // 4))
        # Create a rect with the size of the player image
        self.rect = self.image.get_rect()
        # And immediately set it's x, y cords.
        self.rect.x = (SCREEN.get("width") - self.image.get_width()) // 2
        self.rect.y = SCREEN.get("height") - self.image.get_height() - 10

        self.health_points = 5
        self.projectiles = []

        self.explosions_grp = explosions_grp
        self.sound = sound
        self.aliens = aliens

    def draw(self, surface: pygame.Surface) -> None:
        """
        Draw the player ship on the game screen surface.
        """
        surface.blit(self.image, (self.rect.x, self.rect.y))

    def move_left(self) -> None:
        """
        Move the player ship to the left while it is not hitting the left wall
        """
        # If in contact with left wall do nothing
        if self.rect.x <= 0:
            return
        self.rect.x -= 5

    def move_right(self) -> None:
        """
        Move the player ship to the right while it is not hitting the right wall
        """
        # If in contact with right wall do nothing
        if self.rect.x >= SCREEN.get("width") - self.image.get_width():
            return
        self.rect.x += 5

    def shoot(self) -> None:
        """
        Generate a projectile on the current player x, y coordinates
        """
        # Make sure the player doesn't have an existing projectile on the screen to avoid burst
        if not self.projectiles:
            self.projectiles.append(Projectile(owner=self, x=self.rect.x, y=self.rect.y, vel=8))
            self.sound.play("shoot")

    def take_damage(self) -> None:
        """
        Decrements player health points by 1.
        """
        self.health_points -= 1

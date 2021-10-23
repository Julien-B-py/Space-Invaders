import pygame.sprite


class Alien(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('sprites/alien.png')
        self.image = pygame.transform.scale(self.image, (self.image.get_width() // 4, self.image.get_height() // 4))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.velocity = 1

    def move(self):
        if self.rect.x >= 1280 - self.rect.width or self.rect.x <= 0:
            self.change_direction()
            self.move_down()
        self.rect.x += self.velocity

    def change_direction(self):
        self.velocity = -self.velocity

    def move_down(self):
        self.rect.y += 50

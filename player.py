import pygame.sprite


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("player.png")
        self.image = pygame.transform.scale(self.image, (self.image.get_width() // 4, self.image.get_height() // 4))
        self.x = (1280 - self.image.get_width()) // 2
        self.y = 720 - self.image.get_height() - 10

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

    def move_left(self):
        if self.x <= 0:
            return
        self.x -= 5

    def move_right(self):
        if self.x >= 1280 - self.image.get_width():
            return
        self.x += 5

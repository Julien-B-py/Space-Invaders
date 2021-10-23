import pygame.sprite


class Alien(pygame.sprite.Sprite):
    entities_list = []
    changed_direction = False
    dir_change_cpt = 0

    velocity = 1
    move_down_required = False

    def __init__(self, x, y, sound, aliens_grp):
        super().__init__()
        self.sound = sound
        self.image = pygame.image.load('sprites/alien.png')
        self.image = pygame.transform.scale(self.image, (self.image.get_width() // 4, self.image.get_height() // 4))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.aliens_grp = aliens_grp

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

import pygame.sprite


class Alien(pygame.sprite.Sprite):
    entities_list = []
    changed_direction = False
    dir_change_cpt = 0

    def __init__(self, x, y, sound):
        super().__init__()
        self.sound = sound
        self.image = pygame.image.load('sprites/alien.png')
        self.image = pygame.transform.scale(self.image, (self.image.get_width() // 4, self.image.get_height() // 4))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


        self.velocity = 1
        Alien.entities_list.append(self)

    def move(self):
        if self.is_hitting_wall():

            if not Alien.changed_direction:
                for alien in self.entities_list:
                    alien.change_direction()
                    alien.move_down()

                # self.change_direction()
                # self.move_down()
                self.sound.play("move_down")
                Alien.changed_direction = True

            else:
                Alien.dir_change_cpt += 1
                if Alien.dir_change_cpt > 5:
                    Alien.changed_direction = False
                    Alien.dir_change_cpt = 0

        self.rect.x += self.velocity

    def change_direction(self):
        self.velocity = -self.velocity

    def move_down(self):
        self.rect.y += 25

    def is_hitting_wall(self):
        if self.rect.x >= 1280 - self.rect.width or self.rect.x <= 0:
            return True

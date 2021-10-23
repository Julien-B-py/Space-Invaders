import pygame

from config import SCREEN


class Shield:
    def __init__(self, x):
        super().__init__()
        self.image = pygame.image.load("shield.png")
        self.image = pygame.transform.scale(self.image, (self.image.get_width() // 2, self.image.get_height() // 2))
        self.width = self.image.get_width()
        self.x = x
        self.y = SCREEN.get("height")-110
        self.health_points = 20

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))


class ShieldGenerator:
    def __init__(self):
        self.image = pygame.image.load("shield.png")
        self.image = pygame.transform.scale(self.image, (self.image.get_width() // 2, self.image.get_height() // 2))
        self.shield_width = self.image.get_width()

    def generate_shields(self, qty: int = 4) -> list:

        if qty < 0:
            return []

        qty = min(qty, 8)

        space_between_shields = (SCREEN.get("width") - qty * self.shield_width) / (qty + 1)

        created_shields = 0
        all_shields = []

        while True:

            x = round(space_between_shields + (created_shields * (self.shield_width + space_between_shields)))

            # Out of screen
            if x >= SCREEN.get("width"):
                break

            all_shields.append(Shield(x=x))
            created_shields += 1

        return all_shields

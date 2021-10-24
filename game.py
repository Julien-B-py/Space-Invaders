import pygame

from config import SCREEN


class Game:
    def __init__(self):
        self.exit = False
        self.is_over = False
        self.score = 0

        self.background = pygame.image.load("img/bg.jpg")

        self.hud_font = pygame.font.SysFont("Comic Sans MS", 20)
        self.message_font = pygame.font.SysFont("Comic Sans MS", 60)

    def display_player_hp(self, surface, hp):
        hp_text_surface = self.hud_font.render(f"HP: {hp}/5", True, (255, 255, 255))
        surface.blit(hp_text_surface, (10, 10))

    def display_player_score(self, surface):
        score_surface = self.hud_font.render(f"Score: {self.score}", True, (255, 255, 255))
        surface.blit(score_surface, ((SCREEN.get("width") - score_surface.get_width()) / 2, 10))

    def display_end_game_message(self, surface, hp):
        end_text = "YOU LOSE!" if hp == 0 else "YOU WIN!"
        text_surface = self.message_font.render(end_text, True, (255, 255, 255))
        surface.blit(text_surface, ((SCREEN.get("width") - text_surface.get_width()) / 2,
                                    (SCREEN.get("height") - text_surface.get_height()) / 2))

    def increment_score(self, value):
        self.score += value

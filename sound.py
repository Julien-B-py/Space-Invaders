import pygame


class Sound:

    def __init__(self):
        # Create a dict of new Sound objects from audio files
        self.sounds = {
            'explosion': pygame.mixer.Sound("sounds/explosion.ogg"),
            'shoot': pygame.mixer.Sound("sounds/shoot.ogg"),
        }

    def play(self, sound_name):
        """
        Begin specified Sound object playback
        """
        self.sounds[sound_name].play()

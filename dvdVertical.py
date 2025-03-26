import pygame
import random
from dvd import MoveText

class MoveTextVertical(MoveText):
    def __init__(self, text, font_size, initial_color, screen_width, screen_height):
        """Inicializa a classe com seus atributos"""
        self.font = pygame.font.SysFont(None, font_size)
        self.color = initial_color
        self.text = text
        self.text_surf = self.font.render(self.text, True, self.color)
        self.rect = self.text_surf.get_rect(
            center=(screen_width / 2, screen_height / 2)
        )
        self.start_time = pygame.time.get_ticks()
        self.speed_x = 0
        self.speed_y = super().generate_speed()

        self.screen_width = screen_width
        self.screen_height = screen_height

    def update(self):
        """Altera para subir e descer e muda a cor"""
        self.rect.y += self.speed_y

        if self.rect.top <= 0:
            self.speed_y = 1
            super().change_color()

        if self.rect.bottom >= self.screen_height:
            self.speed_y = -1
            super().change_color()


import pygame
import random
from dvd import MoveText

class MoveTextHorizontal(MoveText):
    def __init__(self, text, font_size, initial_color, screen_width, screen_height):
        """Inicializa a classe"""
        self.font = pygame.font.SysFont(None, font_size)
        self.color = initial_color
        self.text = text
        self.text_surf = self.font.render(self.text, True, self.color)
        self.rect = self.text_surf.get_rect(
            center=(screen_width / 2, screen_height / 2)
        )
        self.start_time = pygame.time.get_ticks()
        self.speed_x = super().generate_speed()
        self.speed_y = 0

        self.screen_width = screen_width
        self.screen_height = screen_height

    def update(self):
        """Método para ir para direita e esquerda"""
        self.rect.x += self.speed_x

        if self.rect.left <= 0:
            self.speed_x = random.randint(0, 1)
            super().change_color()

        if self.rect.right >= self.screen_width:
            self.speed_x = random.randint(-1, 0)
            super().change_color() 


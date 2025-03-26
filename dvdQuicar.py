import pygame
import random
from dvd import MoveText
from config import TOP_QUICAR, BOTTOM_QUICAR
from audioController import AudioController

class MoveTextQuicar(MoveText):
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
        self.speed_y = -1

        self.screen_width = screen_width
        self.screen_height = screen_height
        self.audio_controller = AudioController()

    def update(self):
        """Altera para ir para esquerda e direita"""
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.left <= 0:
            self.speed_x = random.randint(0, 1)
            super().change_color()
            super().sound_effect()

        if self.rect.right >= self.screen_width:
            self.speed_x = random.randint(-1, 0)
            super().change_color() 
            super().sound_effect()

        self.quicar()            

    def quicar(self):
        print(self.rect.top)
        """Método para quicar"""
        if self.rect.top <= TOP_QUICAR:
            self.speed_y = 1
            super().change_color() 
        if self.rect.bottom >= BOTTOM_QUICAR:
            self.speed_y = -1     
            super().change_color()            


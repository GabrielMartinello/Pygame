import pygame
import random
from audioController import AudioController

class MoveText:
    def __init__(self, text, font_size, initial_color, screen_width, screen_height):
        self.font = pygame.font.SysFont(None, font_size)
        self.color = initial_color
        self.text = text
        self.text_surf = self.font.render(self.text, True, self.color)
        self.rect = self.text_surf.get_rect(
            center=(screen_width / 2, screen_height / 2)
        )
        self.start_time = pygame.time.get_ticks()
        self.speed_x = self.generate_speed()
        self.speed_y = -1

        self.screen_width = screen_width
        self.screen_height = screen_height
        self.audio_controller = AudioController()

    def generate_speed(self):
        speed_options = [-1, 1]
        return random.choice(speed_options)

    def change_color(self):

        self.color_random = (
            random.randint(10, 255),
            random.randint(10, 255),
            random.randint(10, 255),
        )
        self.color = self.color_random
        self.text_surf = self.font.render(self.text, True, self.color)

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.left <= 0:
            self.speed_x = random.randint(0, 1)
            self.change_color()

        if self.rect.right >= self.screen_width:
            self.speed_x = random.randint(-1, 0)
            self.change_color()

    def draw(self, screen):
        screen.blit(self.text_surf, self.rect)    

    def sound_effect(self):
        self.audio_controller.sound_effect()




            
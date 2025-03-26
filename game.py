import sys
import pygame
from dvd import MoveText
from config import (
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    FPS,
    PRETO,
    BRANCO,
    NAME,
    CAPTION,
    FONT_SIZE
)

from dvdQuicar import MoveTextQuicar
from audioController import AudioController

class Game:
    def __init__(self):
        """Classe principal para rodar o jogo"""
        pygame.init()

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(CAPTION)
        self.clock = pygame.time.Clock()
        self.running = True
        self.text = MoveTextQuicar(NAME, FONT_SIZE, BRANCO, SCREEN_WIDTH, SCREEN_HEIGHT)
        self.audio_controller = AudioController()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        """Altera as posições"""
        self.text.update()

    def draw(self):
        """Desenha a tela"""
        self.screen.fill(PRETO)
        self.text.draw(self.screen)
        pygame.display.flip()

    def run(self):
        """Método para configurações iniciais e comportamentos"""
        self.audio_controller.tocarMuscia()
        while self.running:
            self.events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        pygame.quit()
        sys.exit()
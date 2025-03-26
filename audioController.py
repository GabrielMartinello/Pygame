import os
import pygame

class AudioController:
    """Gerencia a reprodução de músicas e efeitos sonoros no jogo."""
    
    def __init__(self):
        """Inicializa o mixer do pygame e carrega os arquivos de áudio necessários."""
        pygame.mixer.init()
        pygame.mixer.music.load("./sounds/ai-cover.mp3")

    def tocarMuscia(self):
        pygame.mixer.music.play(-1)
      
    def sound_effect(self):
        """Inicia a reprodução do som ao tocar nos cantos"""
        pygame.mixer.Sound("./sounds/canto-do-nip.mp3").play()
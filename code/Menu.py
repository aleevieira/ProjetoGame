#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH


class Menu:
    def __init__(self, window):
        self.window: Surface = window
        self.surf = pygame.image.load('./asset/MenuBG.png')
        # A partir dessa superfície, pegue o retângulo que representa essa superfície e posicione em x/y local
        self.rect = self.surf.get_rect(left=0, top=0)

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_position: tuple):
        text_font: Font = pygame.font.SysFont(name='Lucida Sans Typewrite', size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color)  # gerando a imagem de texto/renderizando
        text_rect: Rect = text_surf.get_rect(center=text_center_position)
        self.window.blit(source=text_surf, dest=text_rect)

    def run(self):
        pygame.mixer_music.load('./asset/Menu.mp3')
        pygame.mixer_music.play(-1)  # o -1 é para rodar indefinidamente
        while True:
            # Desenha a tela, da superfície self.surf (fonte) e vai desenhar no retângulo self.rect
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, "Mountain Shooter", (255, 128, 0), (WIN_WIDTH / 2, 70))  # cores no padrão RGB
            pygame.display.flip()  # atualizar a tela enquanto é desenhada
            pass

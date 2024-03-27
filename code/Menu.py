#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, COLOR_ORANGE, MENU_OPTION, COLOR_WHITE, COLOR_YELLOW


class Menu:
    def __init__(self, window):
        self.window: Surface = window
        self.surf = pygame.image.load('./asset/MenuBG.png')
        # A partir dessa superfície, pegue o retângulo que representa essa superfície e posicione em x/y local
        self.rect = self.surf.get_rect(left=0, top=0)

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_position: tuple):
        text_font: Font = pygame.font.SysFont(name='Lucida Sans Typewriter', size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color)  # gerando a imagem de texto/renderizando
        text_rect: Rect = text_surf.get_rect(center=text_center_position)
        self.window.blit(source=text_surf, dest=text_rect)

    def run(self):
        pygame.mixer_music.load('./asset/Menu.mp3')
        pygame.mixer_music.play(-1)  # o -1 é para rodar indefinidamente
        menu_option = 0
        while True:
            # Desenha a tela, da superfície self.surf (fonte) e vai desenhar no retângulo self.rect
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, "Mountain", COLOR_ORANGE, (WIN_WIDTH / 2, 70))  # cores no padrão RGB
            self.menu_text(50, "Shooter", COLOR_ORANGE, (WIN_WIDTH / 2, 120))

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(20, MENU_OPTION[i], COLOR_YELLOW, (WIN_WIDTH / 2, 200 + 30 * i))
                else:
                    self.menu_text(20, MENU_OPTION[i], COLOR_WHITE, (WIN_WIDTH / 2, 200 + 30 * i))
            pygame.display.flip()  # atualizar a tela enquanto é desenhada

            # Verificar eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:  # testar se alguma tecla for pressionada
                    if event.key == pygame.K_DOWN:  # se a tecla seta para baixo foi pressionada
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP:  # se a tecla seta para baixo foi pressionada
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN:  # Tecla enter, retorna a opção desejada
                        return MENU_OPTION[menu_option]  # retorna com base no texto a opção escolhida



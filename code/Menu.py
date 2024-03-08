#!/usr/bin/python
#-*- coding: utf-8 -*-
import pygame
from pygame import Surface


class Menu:
    def __init__(self, window):
        self.window: Surface = window
        self.surf = pygame.image.load('./asset/MenuBG.png')
        # A partir dessa superfície, pegue o retângulo que representa essa superfície e posicione em x/y local
        self.rect = self.surf.get_rect(left=0, top=0)
    def run(self):
        while True:
            # Desenha a tela, da superfície self.surf (fonte) e vai desenhar no retângulo self.rect
            self.window.blit(source=self.surf, dest=self.rect)
            pygame.display.flip()  # atualizar a tela enquanto é desenhada
            pass


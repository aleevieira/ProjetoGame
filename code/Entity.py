#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod

import pygame.image
from pygame import Surface, Rect


class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surf: Surface = pygame.image.load('./asset/' + name + '.png')
        self.rect: Rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0

    @abstractmethod
    def move(self):
        pass  # Uma classe abstrata não implementa nenhum método. Porém, as classes filhas
        # obrigatoriamente devem implementar este método move.

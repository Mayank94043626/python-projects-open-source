import pygame as pg
from random import uniform


class Particle:
    def __init__(self, pos) -> None:
        self.__pos = pg.Vector2(pos)
        randx = uniform(-4, 4)
        randy = uniform(-14, -1)
        self.__vel = pg.Vector2([randx, randy])
        self.__radius = uniform(1, 7)

    def draw(self, window):
        pg.draw.circle(window, "white", self.__pos, self.__radius)

    def update(self):
        self.__vel.y += 0.4
        self.__pos += self.__vel
        self.__radius -= 0.1

    def is_dead(self):
        return self.__radius <= 0

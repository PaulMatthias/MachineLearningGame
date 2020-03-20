import pygame
import Utils

# Die Player Klasse verwendet zwei Animationen, um eine steuerbare Spielfigur dazustellen.
class Hindernis(object):
    def __init__(self, x, y, v):
        # Bild laden und erste Animation erstellen:
        self.image = Utils.load_image("spike.png", (255, 0, 255))

        # Start-Position des Hindernis festlegen und
        # merken in welche Richtung wir schauen und ob wir überhaupt laufen.
        self.pos_x = x
        self.pos_y = y
        self.vel_x = v
        self.isDeadly = True

    def render(self, screen):
        screen.blit(self.image, (self.pos_x, self.pos_y))

    def move(self):
        self.pos_x = self.pos_x + self.vel_x


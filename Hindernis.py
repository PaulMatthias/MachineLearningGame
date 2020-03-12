import pygame
import Utils

# Die Player Klasse verwendet zwei Animationen, um eine steuerbare Spielfigur dazustellen.
class Hindernis(object):
    def __init__(self):
        # Bild laden und erste Animation erstellen:
        self.image = Utils.load_image("spike.png", (255, 0, 255))

        # Start-Position des Hindernis festlegen und
        # merken in welche Richtung wir schauen und ob wir überhaupt laufen.
        self.pos_x = 10*32
        self.pos_y = 13*32
        self.isDeadly = True

    def render(self, screen):
        # Blickrichtung links rendern.
        self.image.render(screen, (self.pos_x, self.pos_y))


    def handle_input(self, key):
        # Linke Pfeiltaste wird gedrückt:
        if key == 'LEFT':
            # x-Position der Spielfigur anpassen,
            # die Blickrichtung festlegen
            # und den Laufen-Zustand einschalten.
            self.pos_x += 3

        # Und nochmal für die rechte Pfeiltaste.
        if key == 'RIGHT':
            self.pos_x -= 3

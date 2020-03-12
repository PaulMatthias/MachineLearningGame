# -*- coding: UTF-8 -*-

import pygame
import Utils
import Animation

# Die Player Klasse verwendet zwei Animationen, um eine steuerbare Spielfigur dazustellen.
class Player(object):
    def __init__(self):
        # Bild laden und erste Animation erstellen:
        self.anim_image_right = Utils.load_image("tileset.png", (255, 0, 255))
        self.anim_right = Animation.Animation(self.anim_image_right, 32, 32, 2, 32, 64, 15)

        # Die Grafik spiegeln und in einer neuen Surface speichern,
        # dann können wir die linke Animation erstellen.
        self.anim_image_left = pygame.transform.flip(self.anim_image_right, True, False)
        self.anim_left = Animation.Animation(self.anim_image_left, 32, 32, 2, 32, 64, 15)

        # Start-Position des Players festlegen und
        # merken in welche Richtung wir schauen und ob wir überhaupt laufen.
        self.pos_x = 10*32
        self.pos_y = 13*32
        self.pos_x_old = self.pos_x
        self.dir = 0
        self.walking = False

        # Force of gravity and mass
        self.v = 8
        self.m = 2
        self.isjump = False

    def jump(self):
        # Calculate force (F). F = 0.5 * mass * velocity^2.
        if self.v >= 0:
            F = ( 0.5 * self.m * (self.v*self.v) )
        else:
            F = -( 0.5 * self.m * (self.v*self.v) )

        # Change position
        self.pos_y = self.pos_y - F

        # Change velocity
        self.v = self.v - 1

        # If ground is reached, reset variables.
        if self.pos_y > 13*32:
            self.pos_y = 13*32
            self.isjump = False
            self.v = 8

    def render(self, screen):
        # Die Blickrichtung ist links:
        if self.dir == -1:
            # Wenn der Spieler die linke oder rechte Pfeiltaste gedrückt hat sind wir am laufen,
            if self.walking:
                # nur dann die Animation updaten.
                self.anim_left.update()
            # Blickrichtung links rendern.
            self.anim_left.render(screen, (self.pos_x, self.pos_y))
        else:
            # Und das gleiche nochmal für rechts:
            if self.walking:
                self.anim_right.update()
            self.anim_right.render(screen, (self.pos_x, self.pos_y))

        # De Laufen-Zustand zurücksetzen, im nächsten Frame bleiben wir stehen.
        self.walking = False


    def handle_input(self, key):
        # Linke Pfeiltaste wird gedrückt:
        if key == 'LEFT':
            # x-Position der Spielfigur anpassen,
            # die Blickrichtung festlegen
            # und den Laufen-Zustand einschalten.
            self.pos_x -= 3
            self.dir = -1
            self.walking = True

        # Und nochmal für die rechte Pfeiltaste.
        if key == 'RIGHT':
            self.pos_x += 3
            self.dir = 1
            self.walking = True

        if key == 'UP':
            self.isjump = True


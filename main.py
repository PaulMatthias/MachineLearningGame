# -*- coding: UTF-8 -*-

# Pygame Modul importieren.
import pygame

# Unser Tilemap Modul
import Tilemap

import AutoInput

# Überprüfen, ob die optionalen Text- und Sound-Module geladen werden konnten.
if not pygame.font: print('Fehler pygame.font Modul konnte nicht geladen werden!')
if not pygame.mixer: print('Fehler pygame.mixer Modul konnte nicht geladen werden!')

def main():
    # Initialisieren aller Pygame-Module und
    # Fenster erstellen (wir bekommen eine Surface, die den Bildschirm repräsentiert).
    pygame.init()
    screen = pygame.display.set_mode((800, 600))

    # Titel des Fensters setzen, Mauszeiger nicht verstecken und Tastendrücke wiederholt senden.
    pygame.display.set_caption("Pygame-Tutorial: Animation")
    pygame.mouse.set_visible(1)
    pygame.key.set_repeat(1, 30)

    # Clock-Objekt erstellen, das wir benötigen, um die Framerate zu begrenzen.
    clock = pygame.time.Clock()

    # Wir erstellen eine Tilemap.
    map = Tilemap.Tilemap()

    event = AutoInput.AutoInput()

    # Die Schleife, und damit unser Spiel, läuft solange running == True.
    running = True
    while running:
        # Framerate auf 30 Frames pro Sekunde beschränken.
        # Pygame wartet, falls das Programm schneller läuft.
        clock.tick(30)

        # screen Surface mit Schwarz (RGB = 0, 0, 0) füllen.
        screen.fill((198, 209, 255))

        event.generateRandomKeyPress()

        map.handle_input(event.key)

        if map.player.isjump:
            map.player.jump()

        # Die Tilemap auf die screen-Surface rendern.
        map.render(screen)

        # Inhalt von screen anzeigen
        pygame.display.flip()


# Überprüfen, ob dieses Modul als Programm läuft und nicht in einem anderen Modul importiert wird.
if __name__ == '__main__':
    # Unsere Main-Funktion aufrufen.
    main()

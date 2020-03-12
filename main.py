# Pygame Modul importieren.
import pygame
# Unser Tilemap Modul
import Tilemap
import AutoInput
from DQN import DQNAgent
from keras.utils import to_categorical
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np



# Überprüfen, ob die optionalen Text- und Sound-Module geladen werden konnten.
if not pygame.font: print('Fehler pygame.font Modul konnte nicht geladen werden!')
if not pygame.mixer: print('Fehler pygame.mixer Modul konnte nicht geladen werden!')

def main():
    # Initialisieren aller Pygame-Module und
    # Fenster erstellen (wir bekommen eine Surface, die den Bildschirm repräsentiert).
    pygame.init()

    agent = DQNAgent()
    counter_games = 0
    record = 0
    while counter_games < 150:
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
            agent.epsilon = 80 - counter_games
            #get old state
            state_old = agent.get_state(game, player1, food1)
            map.player.pos_x_old = map.player.pos_x

            #perform random actions based on agent.epsilon, or choose the action
            if randint(0, 200) < agent.epsilon:
                final_move = to_categorical(randint(0, 2), num_classes=3)
            else:
                # predict action based on the old state
                prediction = agent.model.predict(state_old.reshape((1,7)))
                final_move = to_categorical(np.argmax(prediction[0]), num_classes=3)

            # Framerate auf 30 Frames pro Sekunde beschränken.
            # Pygame wartet, falls das Programm schneller läuft.
            clock.tick(30)

            # screen Surface mit Schwarz (RGB = 0, 0, 0) füllen.
            screen.fill((198, 209, 255))

            event.generateRandomKeyPress()

            map.handle_input(event.key)

            #continue jump animation after
            if map.player.isjump:
                map.player.jump()

            # Die Tilemap auf die screen-Surface rendern.
            map.render(screen)

            state_new = agent.get_state(game, player1, food1)
            #set treward for the new state
            reward = agent.set_reward(player1, game.crash)
            #train short memory base on the new action and state
            agent.train_short_memory(state_old, final_move, reward, state_new, game.crash)

            # Inhalt von screen anzeigen
            pygame.display.flip()

        agent.remember(state_old, final_move, reward, state_new, game.crash)
        record = get_record(game.score, record)
        if display_option:
            display(player1, food1, game, record)
            pygame.time.wait(speed)

        agent.replay_new(agent.memory)
        counter_games += 1

    agent.model.save_weights('weights.hdf5')
    plot_seaborn(counter_plot, score_plot)


# Überprüfen, ob dieses Modul als Programm läuft und nicht in einem anderen Modul importiert wird.
if __name__ == '__main__':
    # Unsere Main-Funktion aufrufen.
    main()

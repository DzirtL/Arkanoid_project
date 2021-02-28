import pygame
from pygame.locals import *
import os
import operator
import all_players
from pygame import mixer
import arkanoid
import sqlite3
pygame.init()

background = pygame.image.load('pictures/main_back.jpg')
os.environ['SDL_VIDEO_CENTERED'] = '1'

font = '20326.otf'

menu_sound = mixer.Sound('music/move.wav')
pygame.mixer.music.load('music/background.mp3')
playlist = list()
playlist.append("music/background_play2.mp3")
playlist.append("music/background_play.mp3")
playlist.append("music/background.mp3")
pygame.mixer.music.load(playlist.pop())
pygame.mixer.music.queue(playlist.pop())
pygame.mixer.music.set_endevent(pygame.USEREVENT)
pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.1)
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

clock = pygame.time.Clock()
FPS = 60

font = "20326.otf"


def text_format(message, textFont, textSize, textColor):
    newFont = pygame.font.Font(textFont, textSize)
    newText = newFont.render(message, 0, textColor)
    return newText


def upload_leader_board():
    conn = sqlite3.connect('all_players.db')
    c = conn.cursor()
    result = c.execute("""SELECT * FROM leaders""").fetchall()
    conn.commit()
    conn.close()
    leaders = {}
    for i in result:
        leaders[i[0]] = i[1]
    leaders = sorted(leaders.items(), key=lambda kv: kv[1])
    leaders.reverse()
    return leaders


def main_menu():
    global font
    menu = True
    selected = "start"
    first_button = 'Start game'
    second_button = 'Leaders bord'
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.USEREVENT:
                if len ( playlist ) > 0:
                    pygame.mixer.music.queue(playlist.pop())
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected = first_button
                elif event.key == pygame.K_DOWN:
                    selected = second_button
                menu_sound.play(0)
                if event.key == pygame.K_RETURN:
                    if selected == 'Start game':
                        arkanoid.run()
                    if selected == 'Leaders bord':
                        all_players.main(upload_leader_board())
                if event.key == pygame.K_q:
                    menu = False
        screen.blit(background, (0, 0))
        title = text_format("Arkanoid 3000", font, 90, pygame.Color('yellow'))
        if selected == first_button:
            text_arkanoid = text_format(first_button, font, 75, pygame.Color('red'))
        else:
            text_arkanoid = text_format(first_button, font, 75, pygame.Color('white'))
        if selected == second_button:
            text_quit = text_format(second_button, font, 75, pygame.Color('red'))
        else:
            text_quit = text_format(second_button, font, 75, pygame.Color('white'))

        title_rect = title.get_rect()
        start_rect = text_arkanoid.get_rect()
        quit_rect = text_quit.get_rect()

        screen.blit(title, (screen_width/2 - (title_rect[2]/2), 80))
        screen.blit(text_arkanoid, (screen_width/2 - (start_rect[2]/2), 300))
        screen.blit(text_quit, (screen_width/2 - (quit_rect[2]/2), 360))
        pygame.display.update()
        clock.tick(FPS)
        pygame.display.set_caption("Arkanoid 3000")

    pygame.quit()
    quit()


if __name__ == '__main__':
        main_menu()

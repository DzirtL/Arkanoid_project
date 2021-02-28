import pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
font = pygame.font.Font('20326.otf', 65)


def displaytext(text, x, y, color):
    text = font.render(text, 1, color)
    textpos = (x, y)
    screen.blit(text, textpos)


def main():
    player_name = ''
    bg = pygame.image.load('pictures/enter_name.png')
    runGame = True
    while runGame:
        screen.blit(bg, (0, 0))
        displaytext('Enter your name', 20, 30, pygame.Color('yellow'))
        displaytext('and press "Enter"', 20, 100, pygame.Color('yellow'))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runGame = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return player_name
                if event.key == pygame.K_BACKSPACE:
                    player_name = player_name[:-1]
                else:
                    player_name += event.unicode
        displaytext(player_name, 100, 300, pygame.Color('violet'))
        pygame.display.flip()
    pygame.quit()

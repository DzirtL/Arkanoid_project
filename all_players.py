import pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
font = pygame.font.Font('20326.otf', 40)


def displaytext(text, x, y, color):
    text = font.render(text, 1, color)
    textpos = (x, y)
    screen.blit(text, textpos)


def main(lst):
    bg = pygame.image.load('pictures/all_players.jpg')
    runGame = True
    while runGame:
        screen.blit(bg, (0, 0))
        displaytext('Press "Q" to exit', 10, 550, pygame.Color('green'))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runGame = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    return
        x = 200
        y = 0
        for i in lst:
            y += 30
            if i[0] != '':
                displaytext(f'{i[0]} - {i[1]}', x, y, pygame.Color('White'))
        pygame.display.flip()
    pygame.quit()

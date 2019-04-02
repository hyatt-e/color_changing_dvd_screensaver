import pygame
import time
from sys import exit


def main_loop():
    pygame.init()
    width, height = 800, 600
    dvdLogo = pygame.image.load("dvd-logo.png")
    dvdLogo = pygame.transform.scale(dvdLogo, (300, 150))
    dvdLogoSpeed = [1,  1]


    screen = pygame.display.set_mode((width, height))
    dvdLogoRect = dvdLogo.get_rect()

    hits = 0

    while True:
        screen.fill(color_changer(hits))
        screen.blit(dvdLogo, dvdLogoRect)
        dvdLogoRect = dvdLogoRect.move(dvdLogoSpeed)

        if dvdLogoRect.left == 0 or dvdLogoRect.right == width:
            dvdLogoSpeed[0] = -dvdLogoSpeed[0]
        if dvdLogoRect.top == 0 or dvdLogoRect.bottom == height:
            dvdLogoSpeed[1] = -dvdLogoSpeed[1]

        if dvdLogoRect.left == 0 and dvdLogoRect.bottom == height:
            if hits != 2:
                hits += 1
            else:
                hits = 0
            screen.fill(color_changer(hits))
        if dvdLogoRect.left == 0 and dvdLogoRect.top == 0:
            if hits != 2:
                hits += 1
            else:
                hits = 0
            screen.fill(color_changer(hits))
        if dvdLogoRect.right == width and dvdLogoRect.bottom == height:
            if hits != 2:
                hits += 1
            else:
                hits = 0
            screen.fill(color_changer(hits))
        if dvdLogoRect.right == width and dvdLogoRect.top == 0:
            if hits != 2:
                hits += 1
            else:
                hits = 0
            screen.fill(color_changer(hits))

        pygame.display.flip()
        time.sleep(10 / 10000)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()


def color_changer(hits):
    backgroundColors = {"red": (255, 0, 0), "green": (0, 255, 0), "blue": (0, 0, 255)}
    if hits == 0:
        return backgroundColors["red"]
    elif hits == 1:
        return backgroundColors["green"]
    elif hits == 2:
        return backgroundColors["blue"]


main_loop()

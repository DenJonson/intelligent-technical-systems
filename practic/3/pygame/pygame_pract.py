import pygame
import sys
from time import sleep

pygame.init()

screen = pygame.display.set_mode((600, 400))
rect = pygame.Rect(10, 10, 50, 50)


def readFile(name_file):
    arrayWithHist = []

    try:
        file = open(name_file, 'r')
    except:
        print("Sistem error, file not open")
    with file:
        lines = file.readlines()
        for line in lines:
            lst = eval(line) 
            arrayWithHist.append(lst)
    
    return arrayWithHist

Array=readFile("data.txt")
flag = 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if(flag):
            for i in Array:
                if i==1:
                    rect.move_ip(4, 0)
                elif i==2:
                    rect.move_ip(-4, 0)
                elif i==3:
                    rect.move_ip(0, 4)
                elif i==4:
                    rect.move_ip(0, -4)
            flag = 0

    pygame.draw.rect(screen, (69, 228, 69), rect, 0)
    pygame.display.update()
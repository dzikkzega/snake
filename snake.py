import pygame, sys, time, random

check_errors = pygame.init()
if check_errors[1] > 0:
    print('[!] {check_errors} error game')
else:
    print('[+] Game successfully initialized')

#======= WINDOWS GAME =======
size_x = 720
size_y = 480

pygame.display.set_caption('Ular makan')
screen = pygame.display.set_mode((size_x, size_y))

while True:
    pygame.display.update()
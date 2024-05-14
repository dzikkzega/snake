import pygame, sys, time, random

check_errors = pygame.init()
if check_errors[1] > 0:
    print('[!] {check_errors} error game')
else:
    print('[+] Game successfully initialized')

#======= WINDOWS GAME =======
size_x = 720
size_y = 360

#title 
pygame.display.set_caption('Ular makan')
screen = pygame.display.set_mode((size_x, size_y))

#======= COLORS =======
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
green = pygame.Color(0, 255, 0)

#background color
screen.fill(white)

#run program
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
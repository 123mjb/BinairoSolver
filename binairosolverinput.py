import pygame
from pygame import *

from binairosolver import *

pygame.init()
DISPLAY_SIZE = tuple(map(lambda i, j: i - j, pygame.display.get_desktop_sizes()[0], (10,50)))  # type: ignore
DISPLAYSURF = pygame.display.set_mode(tuple(DISPLAY_SIZE),pygame.RESIZABLE)
board = [[3,3,3,3,3,3,3,3],[3,3,3,3,3,3,3,3],[3,3,3,3,3,3,3,3],[3,3,3,3,3,3,3,3],[3,3,3,3,3,3,3,3],[3,3,3,3,3,3,3,3],[3,3,3,3,3,3,3,3],[3,3,3,3,3,3,3,3]]
colours = [pygame.Color(0,0,0),pygame.Color(255,255,255),pygame.Color(255,0,0)]
WHITE = pygame.Color(255,255,255)
BLACK = pygame.Color(0,0,0)
RED = pygame.Color(255,0,0)
DISPLAYSURF.fill(WHITE)
running = True
set = 0
mouseloc: tuple[int,int]
while running:
    for i in range(0,len(board)):
        for g in range(0,len(board[i])):
            pygame.draw.rect(DISPLAYSURF,RED,(i*((DISPLAY_SIZE[0]/8*7)/len(board)) +1,g*((DISPLAY_SIZE[1])/len(board[i])) + 1,(DISPLAY_SIZE[0] / 8 * 7) / len(board) - 1,(DISPLAY_SIZE[1] - 20)/len(board[i]) - 1), 0)
            pygame.draw.circle(DISPLAYSURF,
                                colours[board[i][g] if board[i][g] != 3 else board[i][g] - 1],
                                ( i * ((DISPLAY_SIZE[0] / 8 * 7) / len(board)) + 1 + (((DISPLAY_SIZE[0] / 8 * 7) / len(board) - 1) / 2),
                                 g * ((DISPLAY_SIZE[1]) / len(board[i])) +((DISPLAY_SIZE[1]) / len(board[i])- 1) / 2),
                                ((DISPLAY_SIZE[0] / 8 * 7) / len(board)) / 2 - 2 if ((DISPLAY_SIZE[0] / 8 * 7) / len(board)) < ((DISPLAY_SIZE[1]) / len(board[i]) - 1) else ((DISPLAY_SIZE[1]) / len(board[i]) - 1) / 2 - 2, 0)
            pygame.draw.rect(DISPLAYSURF,RED,(DISPLAY_SIZE[0]/8*7 + 1,1,DISPLAY_SIZE[0]/8-1,DISPLAY_SIZE[1]),0)
    pygame.display.update()
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  running = False
        if event.type == MOUSEBUTTONDOWN and((not pygame.mouse.get_pressed(num_buttons=5)[3]) or (not pygame.mouse.get_pressed(num_buttons=5)[4])):
            if pygame.mouse.get_pressed(num_buttons=3)[0]: set = 1
            elif pygame.mouse.get_pressed(num_buttons=3)[1]: set = 0
            elif pygame.mouse.get_pressed(num_buttons=3)[2]: set = 3
            mouseloc = pygame.mouse.get_pos()
            for i in range(0,len(board)):
                for g in range(0,len(board[i])):
                    if mouseloc[0]>=i*((DISPLAY_SIZE[0]/8*7)/len(board)) +1 and mouseloc[0]<=i*((DISPLAY_SIZE[0]/8*7)/len(board)) +1 + (DISPLAY_SIZE[0] / 8 * 7) / len(board) - 1 and mouseloc[1] >= g*((DISPLAY_SIZE[1])/len(board[i])) + 1 and mouseloc[1] <= g*((DISPLAY_SIZE[1]-20)/len(board[i])) + 1 + (DISPLAY_SIZE[1] - 20)/len(board[i]) - 1: board[i][g]=set
            if mouseloc[0]>=DISPLAY_SIZE[0]/8*7 + 1 and mouseloc[0] <= DISPLAY_SIZE[0]/8*7 + 1+ DISPLAY_SIZE[0]/8-1 and mouseloc[1]>=1 and mouseloc[1]<=1+DISPLAY_SIZE[1]: board = solve(board)


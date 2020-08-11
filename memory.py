import pygame
from math import prod
import random as rd
import numpy as np

# Dimensions
picture_size = [1920,1280]
screen_factor = 3
screen_size = [int(x/screen_factor) for x in picture_size]
cards_distribution = [6,3]
cards_number = prod(cards_distribution)
cards_size = [int(x/y) for x, y in zip(screen_size,cards_distribution)]

class Card():
    def __init__(self,pos,number):
        self.pos = pos
        self.color = (255,255,255)
        self.border_color = (255,0,0)
        self.border_width = 3
        self.margin = 2
        self.number = number
        # self.font = pygame.font.Font('freesansbold.ttf', 40)
        self.font = pygame.font.SysFont('ubuntu',70)
        self.text = self.font.render(str(self.number), True, self.border_color)
        self.text_center_x = self.pos[0]+cards_size[0]/2
        self.text_center_y = self.pos[1]+cards_size[1]/2
        self.text_rect = self.text.get_rect(center=(self.text_center_x, self.text_center_y))

    def draw_card(self,surface):
        pygame.draw.rect(
            surface, self.border_color, 
            (self.pos[0]+self.margin, self.pos[1]+self.margin, \
                cards_size[0]-2*self.margin,\
                cards_size[1]-2*self.margin)
            )
        pygame.draw.rect(
            surface, self.color, 
            (self.pos[0]+self.margin+self.border_width, \
                self.pos[1]+self.margin+self.border_width, \
                cards_size[0]-2*self.margin-2*self.border_width, \
                cards_size[1]-2*self.margin-2*self.border_width)
            )
    def turn(self,screen):
        screen.blit(self.text, self.text_rect)

def update_screen(img, screen, card_dict,Trying):
    pygame.display.update()
    screen.blit(img, (0,0))
    for c in card_dict.values():
        c[0].draw_card(screen)

def main_memory():
    # Trying = True
    pygame.init()
    screen = pygame.display.set_mode(screen_size)
    img = pygame.image.load('figures/6_WinningPicture.jpg')

    # Create dictionary
    card_dict = {}; i = 0
    card_number = np.array(range(1,int(cards_number/2)+1))
    card_number = np.append(card_number,card_number)
    rd.shuffle(card_number)
    for x in range(cards_distribution[0]):
        for y in range(cards_distribution[1]):
            pipe_id = str(cards_size[0]*x)+'_'+str(cards_size[1]*y)
            card_dict[pipe_id] = [
                Card([cards_size[0]*x,cards_size[1]*y],card_number[i]),
                card_number[i]
            ]
            i += 1
    
    while True:
        update_screen(img, screen, card_dict,False)
        e = pygame.event.wait()
        if e.type == pygame.MOUSEBUTTONDOWN:
            break
        if e.type == pygame.QUIT:
            quit()

    last_card_id = 0; game = True
    while game:
        e = pygame.event.wait()

        if e.type == pygame.QUIT:
            quit()
        if e.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            x_card = int(mx/cards_size[0])*cards_size[0]
            y_card = int(my/cards_size[1])*cards_size[1]
            pipe_id = str(x_card)+'_'+str(y_card)
            if pipe_id in card_dict.keys():
                card_dict[pipe_id][0].turn(screen)
                if last_card_id != pipe_id and last_card_id != 0 and \
                    card_dict[pipe_id][1] == card_dict[last_card_id][1]:
                        card_dict.pop(pipe_id)
                        card_dict.pop(last_card_id)
                        last_card_id = 0
                        update_screen(img, screen, card_dict,True)
                else:
                    last_card_id = pipe_id
            update_screen(img, screen, card_dict,True)

        if len(card_dict) == 0:
            game = False

            
            
                    
main_memory()
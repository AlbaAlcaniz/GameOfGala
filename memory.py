import pygame
import time
from math import prod
from random import shuffle
from numpy import array, append


class Card():
    """Class for the card objects
    """
    global cards_size

    def __init__(self,pos,number,cards_size):
        """Initialize the card by giving its position inside the screen and the
        number that appears when it is turned.

        Args:
            pos (list): x and y position of the top left of the card
            number (int): number that is displayed when the card is turned
        """
        self.pos = pos
        self.cards_size = cards_size
        self.color = (255,255,255)
        self.border_color = (255,0,0)
        self.border_width = 3
        self.margin = 2
        self.number = number
        self.font = pygame.font.SysFont('ubuntu',70)
        self.text = self.font.render(str(self.number), True, self.border_color)
        self.text_center_x = int(self.pos[0]+cards_size[0]/2)
        self.text_center_y = int(self.pos[1]+cards_size[1]/2)
        self.text_rect = self.text.get_rect(center=(self.text_center_x, 
                                                    self.text_center_y))

    def draw_card(self,surface):
        """Draw the card by using pygame commands. The card is a white 
        rectangle with a red border.

        Args:
            surface (pygame.Surface): window where the cards are displayed.
        """
        pygame.draw.rect(
            surface, self.border_color, 
            (self.pos[0]+self.margin, self.pos[1]+self.margin, \
                self.cards_size[0]-2*self.margin,\
                self.cards_size[1]-2*self.margin)
        )
        pygame.draw.rect(
            surface, self.color, 
            (self.pos[0]+self.margin+self.border_width, \
                self.pos[1]+self.margin+self.border_width, \
                self.cards_size[0]-2*self.margin-2*self.border_width, \
                self.cards_size[1]-2*self.margin-2*self.border_width)
        )

    def turn(self,screen):
        """Function that displays the number of the card, simulating that the
        card is turned around

        Args:
            screen (pygame.Surface): window where the cards are displayed.
        """
        screen.blit(self.text, self.text_rect)


class MainScreen():
    def __init__(self,screen_size):
        self.screen = pygame.display.set_mode(screen_size,pygame.RESIZABLE,0,32)
        self.bg_img = pygame.image.load('figures/6_WinningPicture.jpg')
        self.bg_img2 = pygame.image.load('figures/6_WinningPicture2.jpg')

    def initial_setup(self,card_dict):
        pygame.display.update()
        self.screen.blit(self.bg_img, (0,0))
        for c in card_dict.values():
            c[0].draw_card(self.screen)

    def new_configuration(self):
        pygame.display.set_mode([640,616],pygame.RESIZABLE,0,32)
        self.text = ''
        self.font = pygame.font.SysFont('calibri',48)
        self.text_color = (0,0,0)
        self.img_text = self.font.render(self.text, True, self.text_color)

        self.rect = self.img_text.get_rect()
        self.rect.topleft = (20, 550)
        self.cursor = pygame.Rect(self.rect.topright, (3, self.rect.height))

    def modify_text(self,event):
        if event.key == pygame.K_BACKSPACE:
            if len(self.text)>0:
                self.text = self.text[:-1]
        else:
            self.text += event.unicode

        self.img_text = self.font.render(self.text, True, self.text_color)
        self.rect.size=self.img_text.get_size()
        self.cursor.topleft = self.rect.topright

    def new_setup(self):
        self.screen.blit(self.bg_img2, (0,0))
        self.screen.blit(self.img_text, self.rect)
        if time.time() % 1 > 0.5:
            pygame.draw.rect(self.screen, self.text_color, self.cursor)
        pygame.display.update()


class Deck():
    def __init__(self,screen_size):
        # cards_distribution = [6,3]
        self.cards_distribution = [2,1]
        self.number_of_cards = prod(self.cards_distribution)
        self.cards_size = [
            int(x/y) for x, y in zip(screen_size,self.cards_distribution)
            ]
        self.create_cards_dictionary()
        self.last_card_id = 0

    def create_cards_dictionary(self):
        """Function that creates a dictionary of the cards which are identified by
        its position and the number that appears on each card is also displayed

        Returns:
            dictionary: already mentioned dictionary of cards
        """
        self.card_dict = {}; i = 0
        card_number = array(range(1,int(self.number_of_cards/2)+1))
        card_number = append(card_number,card_number)
        shuffle(card_number)
        for x in range(self.cards_distribution[0]):
            for y in range(self.cards_distribution[1]):
                pipe_id = str(self.cards_size[0]*x)+'_'+ \
                    str(self.cards_size[1]*y)
                self.card_dict[pipe_id] = [
                    Card([self.cards_size[0]*x,self.cards_size[1]*y], \
                        card_number[i],self.cards_size),
                    card_number[i]
                ]
                i += 1
        return self.card_dict

    def identify_card(self,screen):
        mx, my = pygame.mouse.get_pos()
        x_card = int(mx/self.cards_size[0])*self.cards_size[0]
        y_card = int(my/self.cards_size[1])*self.cards_size[1]
        pipe_id = str(x_card)+'_'+str(y_card)
        if pipe_id in self.card_dict.keys():
            self.card_dict[pipe_id][0].turn(screen.screen)
            if self.last_card_id != pipe_id and self.last_card_id != 0 and \
                self.card_dict[pipe_id][1] == self.card_dict[self.last_card_id][1]:
                    self.card_dict.pop(pipe_id)
                    self.card_dict.pop(self.last_card_id)
                    self.last_card_id = 0
                    screen.initial_setup(self.card_dict)
            else:
                self.last_card_id = pipe_id


def main_memory():
    """Main function for the classic memory game, where a series of the cards 
    are laid face down on a surface and one card is flipped face up over each
    turn. The object of the game is to turn over pairs of matching cards.
    """
    # Dimensions
    screen_size = [640,426]

    pygame.init()
    deck_cards = Deck(screen_size)
    card_dict = deck_cards.create_cards_dictionary()
    screen = MainScreen(screen_size)

    while True:
        e = pygame.event.wait()
        if e.type == pygame.MOUSEBUTTONDOWN:
            break
        if e.type == pygame.QUIT:
            quit()
        screen.initial_setup(deck_cards.card_dict)

    game = True
    while game:
        e = pygame.event.wait()
        if e.type == pygame.QUIT:
            quit()
        if e.type == pygame.MOUSEBUTTONDOWN:
            deck_cards.identify_card(screen)
            screen.initial_setup(card_dict)

        if len(card_dict) == 0:
            game = False
            
    screen.new_configuration()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
                screen.modify_text(event)
        screen.new_setup()

        if screen.text.upper() == 'FERNAN':
            running = False
            pygame.quit()


# main_memory()
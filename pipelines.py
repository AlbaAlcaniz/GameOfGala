import pygame
from time import time
from numpy import array


class Pipe():
    """Class for the green pipe objects which can be turned around.
    """
    def __init__(self, abs_pos, angle, correct_angle, bended):
        """Initialize each pipe by knowing its position, angle, correct angle
        and whether they are bended or straight.

        Args:
            abs_pos (tuple): position of the pipe in the window
            angle (int): initial angle of the pipe, which represents the
                rotation with respect to the original figure
            correct_angle (int): angle in which the pipe makes the circuit
                continuos
            bended (bool): States whether the pipe is straight or bended
        """
        self.abs_pos = abs_pos
        self.angle = angle
        self.correct_angle = correct_angle
        self.bended = bended
        if bended:
            self.original_image = pygame.image.load('figures/6_2_bended_pipe.png')
        else:
            self.original_image = pygame.image.load('figures/6_2_str_pipe.png')
        self.image = self.original_image
        self.rect = self.image.get_rect().move(self.abs_pos)

    def draw_pipe(self, screen):
        """Rotate the image considering its angle and display it on the screen

        Args:
            screen (pygame.Surface): window where the game is displayed.
        """
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        screen.blit(self.image, self.rect)

    def turn_pipe(self):
        """Rotate the image by adding 270 degrees to the pipe's angle
        """
        if self.bended:
            self.angle = (self.angle+270)%360
        else:
            self.angle = (self.angle+270)%180
        

class Pipes:
    """Class for the creation of the dictionary of pipes, where the pipe
    objects are kept
    """
    str_pos = [[5,0],[4,6],[1,2],[2,5],[2,6],[1,4],[0,4]]
    str_ang = [0,0,0,0,0,90,90]
    str_corr_ang = [90,90,90,90,90,0,0]    
    bend_pos = [[0,2],[5,4],[2,4],[6,5],[3,2],[5,1],[6,2],[4,5],
        [2,2],[4,3],[1,1],[1,3],[6,3],[2,3]]
    bend_corr_ang = [180,0,180,270,180,0,270,270,270,0,270,0,0,90]
    bend_ang = [270,0,90,0,270,270,0,0,90,180,0,180,270,270]

    # str_pos = [[5,0],[4,6]]
    # str_ang = [0,0]
    # str_corr_ang = [90,90,90,90,90,0,0]    
    # bend_pos = [[0,2],[5,4]]
    # bend_corr_ang = [180,0]
    # bend_ang = [270,0]

    def __init__(self,square_width):
        """Initialize the class by creating the dictionaries for the straight
        and bended pipes

        Args:
            square_width (int): width of the square that each pipe occupies
        """
        self.square_width = square_width
        self.d_str = self.create_pipes_dictionary(
            self.str_pos, self.str_ang, self.str_corr_ang, False
            )
        self.d_bend = self.create_pipes_dictionary(
            self.bend_pos, self.bend_ang, self.bend_corr_ang, True
            )

    def create_pipes_dictionary(self, positions, ang, corr_ang, bended):
        """Create a dictionary for the pipes, in which the pipe objects are
        saved following an identification code. The state (representing the
        correct rotation of the pipe) in which the pipe is is also saved in the 
        dictionary

        Args:
            positions (list): list of positions of all the pipes
            ang (list): list of angles of all the pipes
            corr_ang (list): list of correct angles of all the pipes
            bended (bool): whether the pipes are bended or not

        Returns:
            dict: the dictionary of pipe objects and its state
        """
        i = 0; dic = {}
        for pos in positions:
            pipe_id = str(int(pos[0])) + '_' + str(int(pos[1]))
            abs_pos = array(pos)*self.square_width
            dic[pipe_id] = [
                Pipe(abs_pos, ang[i], corr_ang[i], bended),
                ang[i] == corr_ang[i]
            ]
            i += 1
        return dic

    def identify_pipe(self):
        """Convert the position where the player clicked on the screen into a
        pipe identification and check if it corresponds to a movable pipe.
        """
        mx, my = pygame.mouse.get_pos()
        x_card = mx//self.square_width
        y_card = my//self.square_width
        pipe_id = str(x_card)+'_'+str(y_card)
        self.turn_pipe_and_check(pipe_id, self.d_str)
        self.turn_pipe_and_check(pipe_id, self.d_bend)

    def turn_pipe_and_check(self, pipe_id, pipes_dict):
        """Check if the position where the player has clicked on the screen 
        corresponds to a movable pipe. If so, turn this pipe and update the
        state of the turned pipe

        Args:
            pipe_id (str): pipe's identification inside the dictionary
            pipes_dict (dict): dictionary of pipes
        """
        if pipe_id in pipes_dict.keys():
            pipes_dict[pipe_id][0].turn_pipe()
            pipes_dict[pipe_id][1] = pipes_dict[pipe_id][0].correct_angle == \
                pipes_dict[pipe_id][0].angle

class MainScreen():
    """Class for the pygame screen.
    """
    def __init__(self, screen_size):
        """Initialize the screen by setting its size and loading two images

        Args:
            screen_size (list): 2D list representing the width and height of
                the screen
        """
        self.screen = pygame.display.set_mode(screen_size, pygame.RESIZABLE, \
            0, 32)
        self.bg_img = pygame.image.load('figures/6_2_pipelines_background.png')
        self.bg_img2 = pygame.image.load('figures/6_2_pipelines_background2.png')

    def initial_setup(self, pipes_dict):
        """Show the background image and the movable pipes

        Args:
            pipes_dict (dict): dictionary of movable pipes
        """
        self.screen.blit(self.bg_img, (0,0))
        for pipe in pipes_dict.values():
            pipe[0].draw_pipe(self.screen)
        pygame.display.update()

    def new_setup(self, pipes_dict):
        """When the player has completed the circuit, display a bigger image 
        with a space below where the player can write the message found.

        Args:
            pipes_dict (dict): dictionary of movable pipes
        """
        self.screen.blit(self.bg_img2, (0,0))
        self.screen.blit(self.img_text, self.rect)
        for pipe in pipes_dict.values():
            pipe[0].draw_pipe(self.screen)
        if time() % 1 > 0.5:
            pygame.draw.rect(self.screen, self.text_color, self.cursor)
        pygame.display.update()

    def new_configuration(self):
        """When the player has completed the circuit, reconfigure the window so
        that the size is increased and text objects are created where the 
        player can write the found message.
        """
        pygame.display.set_mode([490,600],pygame.RESIZABLE,0,32)
        self.text = ''
        self.font = pygame.font.SysFont('calibri',48)
        self.text_color = (0,0,0)
        self.img_text = self.font.render(self.text, True, self.text_color)

        self.rect = self.img_text.get_rect()
        self.rect.topleft = (20, 550)
        self.cursor = pygame.Rect(self.rect.topright, (3, self.rect.height))

    def modify_text(self,event):
        """Store the text that the player is writing

        Args:
            event (pygame.event): interaction of the player with the keyboard
        """
        if event.key == pygame.K_BACKSPACE:
            if len(self.text)>0:
                self.text = self.text[:-1]
        else:
            self.text += event.unicode

        self.img_text = self.font.render(self.text, True, self.text_color)
        self.rect.size=self.img_text.get_size()
        self.cursor.topleft = self.rect.topright

def main_pipelines():
    """Main function for the pipelines game. A circuit of pipelines is shown
    where some of the pipes are in an incorrect position, therefore the water
    cannot flow properly. The incorrect pipes are shown in green. The player
    needs to turn those pipes by clicking on the screen and complete the
    circuit.
    """
    screen_width = 490
    square_width = 70

    pygame.init()
    screen = MainScreen([screen_width,screen_width])
    p = Pipes(square_width)

    game = True
    while game:
        e = pygame.event.wait()
        if e.type == pygame.QUIT:
            quit()
        if e.type == pygame.MOUSEBUTTONDOWN:
            p.identify_pipe()
        if all(value[1] == True for value in {**p.d_str, **p.d_bend}.values()):
            game = False

        screen.initial_setup({**p.d_str, **p.d_bend})

    screen.new_configuration()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
                screen.modify_text(event)
        screen.new_setup({**p.d_str, **p.d_bend})

        if screen.text.upper() == 'MEDIAS':
            running = False
            pygame.quit()

# main_pipelines()
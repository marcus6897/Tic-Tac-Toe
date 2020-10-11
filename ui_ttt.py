import pygame

RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

def make_2d_list(x, y, default_data):
    my_list = list()
    for i in range(y):
        nested_list = list()
        for j in range(x):
            nested_list.append(default_data)
        my_list.append(nested_list)
    return my_list

class Square:
    def __init__(self, x_pos, y_pos, height, width):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.height = height
        self.width = width

class Circle:
    def __init__(self, x_pos, y_pos, radius):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.radius = radius

class Game:
    def __init__(self, window_name, screen_width, screen_height, fps):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.fps = fps

        self.resolution = (screen_width, screen_height)
        self.done = False
    
        pygame.init()
        pygame.font.init()
        self.display = pygame.display.set_mode(self.resolution)
        pygame.display.set_caption(window_name)
        self.font = pygame.font.SysFont("Arial", 16)
        self.clock = pygame.time.Clock()
        self.x, self.y = pygame.mouse.get_pos()

        # SETUP
        self.grid = make_2d_list(3, 3, 0)
        self.player: int = 1
        self.lookup: dict = {
            1: (0,0), 2: (0,1), 3: (0,2),
            4: (1,0), 5: (1,1), 6: (1,2),
            7: (2,0), 8: (2,1), 9: (2,2)
        }
        self.shapes = []
        self.p_height = self.screen_height / 10
        self.p_width = self.screen_width / 10
        self.p_radius = self.screen_width / 20
        self.vertical_grid_line_width = self.screen_width / 40
        self.horizontal_grid_line_height = self.screen_width / 40
        self.allowed_to_play = True

    def reset(self):
        self.grid = make_2d_list(3, 3, 0)
        self.shapes = []
        self.allowed_to_play = True

    def undo(self): # use pop() to remove from shapes[], but also need to remove the drawing
        pass
        
    def get_input(self):
        quadrant = 0
        if self.x < (self.screen_width / 3.0): # mouse cursor is in left third of screen
            if self.y < (self.screen_height / 3.0): # mouse cursor is in top third of screen
                quadrant = 1
            elif self.y < (self.screen_height * (2.0 / 3.0)): # mouse cursor is in middle third of screen
                quadrant = 4
            else: # mouse cursor is in bottom third of screen
                quadrant = 7
        elif self.x < (self.screen_width * (2.0 / 3.0)): # mouse cursor is in middle third of screen
            if self.y < (self.screen_height / 3.0): # mouse cursor is in top third of screen
                quadrant = 2
            elif self.y < (self.screen_height * (2.0 / 3.0)): # mouse cursor is in middle third of screen
                quadrant = 5
            else: # mouse cursor is in bottom third of screen
                quadrant = 8
        else: # mouse cursor is in right third of screen
            if self.y < (self.screen_height / 3.0): # mouse cursor is in top third of screen
                quadrant = 3
            elif self.y < (self.screen_height * (2.0 / 3.0)): # mouse cursor is in middle third of screen
                quadrant = 6
            else: # mouse cursor is in bottom third of screen
                quadrant = 9
        i, j = self.lookup[quadrant]
        if self.grid[i][j] != 0:
            return None
        return quadrant
    
    def print_grid(self):
        for nested_list in self.grid:
            for data in nested_list:
                if data == 0:
                    print("_", end=" ")
                elif data == 1:
                    print("X", end=" ")
                elif data == 2:
                    print("O", end=" ")
                else:
                    assert(0, "Only 0, 1, 2.")
            print()
            
    def switch_player(self):
        if self.player == 1:
            self.player = 2
        elif self.player == 2:
            self.player = 1
        else:
            assert(0, "This is a two player game.")
            
    def place_token(self, p_input):
        i,j = self.lookup[p_input]
        if self.grid != 0:
            self.grid[i][j] = self.player
            if self.player == 1:
                self.shapes.append(Square(self.x, self.y, self.p_height, self.p_width))
            elif self.player == 2:
                self.shapes.append(Circle(self.x, self.y, self.p_radius))
            else:
                assert(0, "What did you do?")
        
    def play_turn(self):
        p_input = self.get_input()
        if p_input is None:
            return
        self.place_token(p_input)
        if self.player_has_won():
            print(f"Player {self.player} has won! Press R to reset.")
            self.allowed_to_play = False
            return
        self.switch_player()
            
    def player_has_won(self) -> bool:
        victory_lookup = [
            [1,2,3], [4,5,6], [7,8,9], [1,5,9], [3,5,7], [1,4,7], [2,5,8], [3,6,9]
        ]
        for sublist in victory_lookup:
            i,j = self.lookup[sublist[0]]
            k,l = self.lookup[sublist[1]]
            m,n = self.lookup[sublist[2]]
            if self.grid[i][j] == self.grid[k][l] == self.grid[m][n] == self.player:
                return True
        return False

    def draw_text(self, text: str, x: int, y: int, color_foreground=(255, 255, 255), color_background=None):
        text_surface = self.font.render(text, True, color_foreground, color_background)
        self.display.blit(text_surface, (x, y))

    def fill_rect(self, x, y, width, height, color=(255, 255, 255)):
        # draw rectangle filled with color
        pygame.draw.rect(self.display, color, (x, y, width, height))

    def fill_triangle(self, x0, y0, x1, y1, x2, y2, color=(255, 255, 255)):
        # draw triangle filled with color
        pygame.draw.polygon(self.display, color, ((x0, y0), (x1, y1), (x2, y2)))

    def draw_line(self, x0, y0, x1, y1, color=(255, 255, 255)):
        # draw line
        pygame.draw.line(self.display, color, (x0, y0), (x1, y1))

    def draw_circle(self, x, y, radius, color=(255, 255, 255)):
        # draw a circle, given that x,y is the top left corner of the circumscribing square
        pygame.draw.circle(self.display, color, (int(x), int(y)), int(radius))

    def play(self):
        while not self.done:                                # loop once per frame
            self.x, self.y = pygame.mouse.get_pos()         # get mouse x, y in px as integers

            # window events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:               # X button pressed
                    self.done = True
                elif event.type == pygame.KEYDOWN:
                    pass
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_r:             # look up keys, pygame.K_<your key>
                        self.reset()
                    elif event.key == pygame.K_u:
                        self.undo()
                elif event.type == pygame.MOUSEBUTTONUP:
                    pass
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if   event.button == 1:                 # left click
                        self.play_turn()
                    elif event.button == 2:                 # middle click
                        pass
                    elif event.button == 3:                 # right click
                        pass
                    elif event.button == 4:                 # scroll up
                        pass
                    elif event.button == 5:                 # scroll down
                        pass
            if self.allowed_to_play:
                self.fill_rect(0, 0, self.screen_width, self.screen_height, (0, 0, 0)) # clear the screen before drawing
            else:
                self.fill_rect(0, 0, self.screen_width, self.screen_height, GREEN)
            # BEGIN UPDATE
            self.fill_rect(x=(self.screen_width / 3) - (self.vertical_grid_line_width / 2), y=0, width=self.vertical_grid_line_width, height=self.screen_height)
            self.fill_rect(x=(self.screen_width * (2 / 3) - (self.vertical_grid_line_width / 2)), y=0, width=self.vertical_grid_line_width, height=self.screen_height)
            self.fill_rect(x=0, y=(self.screen_height / 3) - (self.horizontal_grid_line_height / 2), width=self.screen_width, height=self.horizontal_grid_line_height)
            self.fill_rect(x=0, y=(self.screen_height * (2 / 3) - (self.horizontal_grid_line_height / 2)), width=self.screen_width, height=self.horizontal_grid_line_height)

            for shape in self.shapes: # redraws every previously placed shape after screen clear
                if isinstance(shape, Circle):
                    self.draw_circle(shape.x_pos - shape.radius // 3, shape.y_pos - shape.radius // 3, shape.radius, RED)
                elif isinstance(shape, Square):
                    self.fill_rect(shape.x_pos - (shape.width / 2), shape.y_pos - (shape.height / 2), shape.width, shape.height, BLUE)
                else:
                    assert(0, "¯\_(ツ)_/¯")
            
            if self.allowed_to_play:
                if self.player == 1: # track cursor movement
                    self.fill_rect(self.x - (self.p_width / 2), self.y - (self.p_height / 2), self.p_width, self.p_height, BLUE)
                elif self.player == 2:
                    self.draw_circle(self.x - (self.p_radius // 3), self.y - (self.p_radius // 3), self.p_radius, RED)
                else:
                    assert(0, "¯\_(ツ)_/¯")
            # END UPDATE
            pygame.display.update()                         # put all changes to the screen, call @ end of frame
            self.clock.tick(self.fps)                       # ensure FPS

if __name__ == "__main__":
    game = Game("Bset Gaem", 1920, 1080, 60)
    game.play()

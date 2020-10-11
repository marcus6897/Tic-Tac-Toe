import pygame

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
        self.setup()

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
        pygame.draw.circle(self.display, color, (x, y), radius)

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
                    if event.key == pygame.K_a:             # look up keys, pygame.K_<your key>
                        pass
                    # elif ...
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pass
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if   event.button == 1:                 # left click
                        pass
                    elif event.button == 2:                 # middle click
                        pass
                    elif event.button == 3:                 # right click
                        pass
                    elif event.button == 4:                 # scroll up
                        pass
                    elif event.button == 5:                 # scroll down
                        pass
            self.fill_rect(0, 0, self.screen_width, self.screen_height, (0, 0, 0)) # clear the screen before drawing
            # BEGIN UPDATE

            self.update()

            # END UPDATE
            pygame.display.update()                         # put all changes to the screen, call @ end of frame
            self.clock.tick(self.fps)                       # ensure FPS

    def setup(self):
        pass

    def update(self):
        self.draw_text("Hello there!", self.x, self.y)

if __name__ == "__main__":
    game = Game("Cool Name", 800, 600, 60)
    game.play()
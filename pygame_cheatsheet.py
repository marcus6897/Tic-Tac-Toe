import pygame

screen_width = 800
screen_height = 600
resolution = (screen_width, screen_height)
FPS = 60
done = False

pygame.init()                                 # start pygame
pygame.font.init()                            # do if you want fonts after init
display = pygame.display.set_mode(resolution) # used to pass into draw functions
pygame.display.set_caption("Cool Name")       # set the name of your window
clock   = pygame.time.Clock()

while not done:
    x, y = pygame.mouse.get_pos() # get mouse x, y in px as integers
    # traverse events
    for event in pygame.event.get():
        if event.type   == pygame.QUIT:            pass # X button pressed
        elif event.type == pygame.KEYDOWN:         pass
        elif event.type == pygame.KEYUP:           pass
            if event.key == pygame.K_a:            pass # look up keys, pygame.K_<your key>
        elif event.type == pygame.MOUSEBUTTONDOWN: pass
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if   event.button == 1: pass # left click
            elif event.button == 2: pass # middle click
            elif event.button == 3: pass # right click
            elif event.button == 4: pass # scroll up
            elif event.button == 5: pass # scroll down
    pygame.display.update() # put all changes to the screen, call @ end of frame
    clock.tick(FPS)

def font_get():
    return pygame.font.SysFont("Arial", 12)

def font_draw(font, text: str, x: int, y: int, color_foreground=(255, 255, 255), color_background=None):
    text_surface = font.render(text, True, color_foreground, color_background)
    display.blit(text_surface, x, y)

def fill_rect(x, y, width, height, color=(255, 255, 255)):
    # draw rectangle filled with color
    area = [x, y, width, height]
    pygame.draw.rect(display, color, area)

def fill_triangle(x0, y0, x1, y1, x2, y2, color=(255, 255, 255)):
    # draw triangle filled with color
    pointlist = [(x0, y0), (x1, y1), (x2, y2)]
    pygame.draw.polygon(display, color, pointlist)

def draw_line(x0, y0, x1, y1, color=(255, 255, 255)):
    # draw line
    pygame.draw.line(display, color, (x0, y0), (x1, y1))

def draw_circle(x, y, radius, color=(255, 255, 255)):
    # draw a circle, given that x,y is the top left corner of the surrounding square
    pygame.draw.circle(display, color, (x, y), radius)

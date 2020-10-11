import pygame

FPS = 60
screen_width = 800
screen_height = 600

resolution = (screen_width, screen_height)
done = False

pygame.init()
display = pygame.display.set_mode(resolution) # create screen

clock = pygame.time.Clock() # maintains our FPS


def fill_rect(x, y, width, height, color=(255, 255, 255)):
    # draw rectangle filled with color
    pygame.draw.rect(display, color, (x, y, width, height))

def fill_triangle(x0, y0, x1, y1, x2, y2, color=(255, 255, 255)):
    # draw triangle filled with color
    pygame.draw.polygon(display, color, ((x0, y0), (x1, y1), (x2, y2)))

def draw_line(x0, y0, x1, y1, color=(255, 255, 255)):
    # draw line
    pygame.draw.line(display, color, (x0, y0), (x1, y1))

def draw_circle(x, y, radius, color=(255, 255, 255)):
    # draw a circle, given that x,y is the top left corner of the circumscribing square
    pygame.draw.circle(display, color, (x, y), radius)

while not done:
    mouse_x, mouse_y = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:               # X button pressed
            done = True
        elif event.type == pygame.KEYDOWN:
            pass
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a: # look up keys, pygame.K_<your key>
                pass
            # elif ...
        elif event.type == pygame.MOUSEBUTTONUP:
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
    # blank the screen
    fill_rect(0, 0, screen_width, screen_height, (0, 0, 0))


    fill_rect(mouse_x, mouse_y, 50, 50)


    pygame.display.update() # put all drawing onto the screen
    clock.tick(FPS)

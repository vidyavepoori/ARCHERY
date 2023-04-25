###### _____________ARCHARY PROJECT________________######
# Author List:		[ vidya vepoori, niklesh]
# Filename:			archery_2.py

# import lib
import pygame
import random
import sys

# intilizing pygame
pygame.init()

# Get the dimensions of the user's screen
screen_info = pygame.display.Info()
screen_width = screen_info.current_w
screen_height = screen_info.current_h

screen_size = (1000, 1000)
blank_screen = pygame.Surface(screen_size)
blank_screen.fill((205, 133, 63))


# Set the Pygame display mode to full screen
screen = pygame.display.set_mode(
    (screen_width, screen_height), pygame.FULLSCREEN)
screen.fill((0, 255, 255))
# create blank screen for score board
#  dimension
score_size = (520, 900)
score_surf = pygame.Surface(score_size)  # create a surface
score_surf.fill((234, 213, 211))  # fill color
surf_pos = (1200, 50)  # start pos on screen
surface_rect = pygame.Rect(surf_pos, score_size)
screen.blit(score_surf, surface_rect)
screen.blit(blank_screen, (0, 0))

# Create font object
font_size = 40  # replace with your desired font size
font = pygame.font.Font(None, font_size)

# To map rectangle coord to squar
# Formula is ((x/y_coord/user_screen_size)*required_dimension))


def map_coords_to_rect(x, y):
    x_new = int((x / 1920) * 1001)
    y_new = int((y / 1080) * 1001)
    return (x_new, y_new)


def archery_target():

    target_dim = (900, 900)

    # Set the colors for the target
    colors = [(255, 255, 255), (255, 255, 254), (0, 0, 0), (0, 0, 1), (0, 0, 255),
              (0, 0, 254), (255, 0, 0), (254, 0, 0), (255, 255, 0), (255, 254, 0)]

    # Set the sizes for the circles in the target
    circle_sizes = [target_dim[0] // 20 * i for i in range(10, 0, -1)]

    # Set the position of the target on the screen
    target_x = 500
    target_y = 500

    # Draw the circles in the target
    for i in range(10):

        white = (255,254,255)
        black = (0,0,2)

        circle_size = circle_sizes[i]
        circle_color = colors[i]
        circle_position = (target_x, target_y)
        if i == 3:
            pygame.draw.circle(screen, circle_color, circle_position, circle_size)
            pygame.draw.circle(screen, white, circle_position, circle_size+2, 2)
        else:    
            pygame.draw.circle(screen, circle_color, circle_position, circle_size)
            pygame.draw.circle(screen, black, circle_position, circle_size+2, 2)
    # Draw the plus sign in the center of the target
    plus_size = 20
    plus_color = (128, 128, 128)
    plus_x = target_x
    plus_y = target_y
    pygame.draw.rect(screen, plus_color, pygame.Rect(
        plus_x - plus_size//2, plus_y - plus_size//10, plus_size, plus_size//5))
    pygame.draw.rect(screen, plus_color, pygame.Rect(
        plus_x - plus_size//10, plus_y - plus_size//2, plus_size//5, plus_size))


def text(new_x, new_y):

    # Draw dot at mouse coordinates
    dot_radius = 3  # replace with your desired dot radius
    dot_color = (0, 100, 0)
    pygame.draw.circle(screen, dot_color, (new_x, new_y), dot_radius)
    # Blit text surface onto screen surface
    text_x = new_x + dot_radius + 5  # adjust x position of text
    text_y = new_y - font_size//2  # center text vertically


def target_scored(x, y):

    pixel_color = screen.get_at((x, y))
    print("pixel : ", pixel_color)

    if pixel_color == (255, 254, 0, 255) or pixel_color == (128, 128, 128, 255):  # yellow

        # Create text surface with coordinates
        text_color = (0, 100, 0)  # set color
        text(x, y)
        text_surface = font.render(f"10", True, text_color)
        screen.blit(text_surface, (x, y))

    if pixel_color == (255, 255, 0, 255):  # yellow

        # Create text surface with coordinates
        text_color = (0, 100, 0)  # set color
        text(x, y)
        text_surface = font.render(f"9", True, text_color)
        screen.blit(text_surface, (x, y))

    if pixel_color == (254, 0, 0, 255):  # red

        # Create text surface with coordinates
        text_color = (0, 100, 0)  # set color
        text(x, y)
        text_surface = font.render(f"8", True, text_color)
        screen.blit(text_surface, (x, y))

    if pixel_color == (255, 0, 0, 255):  # red

        # Create text surface with coordinates
        text_color = (0, 100, 0)  # set color
        text(x, y)
        text_surface = font.render(f"7", True, text_color)
        screen.blit(text_surface, (x, y))

    if pixel_color == (0, 0, 254, 255):  # blue

        # Create text surface with coordinates
        text_color = (0, 100, 0)  # set color
        text(x, y)
        text_surface = font.render(f"6", True, text_color)
        screen.blit(text_surface, (x, y))

    if pixel_color == (0, 0, 255, 255):  # blue

        # Create text surface with coordinates
        text_color = (0, 100, 0)  # set color
        text(x, y)
        text_surface = font.render(f"5", True, text_color)
        screen.blit(text_surface, (x, y))

    if pixel_color == (0, 0, 1, 255):  # black

        # Create text surface with coordinates
        text_color = (0, 100, 0)  # set color
        text(x, y)
        text_surface = font.render(f"4", True, text_color)
        screen.blit(text_surface, (x, y))

    if pixel_color == (0, 0, 0, 255):  # black

        # Create text surface with coordinates
        text_color = (0, 100, 0)  # set color
        text(x, y)
        text_surface = font.render(f"3", True, text_color)
        screen.blit(text_surface, (x, y))

    if pixel_color == (255, 255, 254, 255):  # white

        # Create text surface with coordinates
        text_color = (0, 100, 0)  # set color
        text(x, y)
        text_surface = font.render(f"2", True, text_color)
        screen.blit(text_surface, (x, y))

    if pixel_color == (255, 255, 255, 255):  # white

        # Create text surface with coordinates
        text_color = (0, 100, 0)  # set color
        text(x, y)
        text_surface = font.render(f"1", True, text_color)
        screen.blit(text_surface, (x, y))

    if pixel_color == (205, 133, 63, 255) or pixel_color ==(0,255,255,255):  # brown

        # Create text surface with coordinates
        text_color = (0, 100, 0)  # set color
        text(x, y)
        text_surface = font.render(f":(", True, text_color)
        screen.blit(text_surface, (x, y))


# Wait for the user to close the window
done = False
archery_target()

# Main loop
while True:

    # Handle Pygame events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.MOUSEBUTTONUP:

            # Get mouse coordinates
            mouse_x, mouse_y = pygame.mouse.get_pos()
            new_x, new_y = map_coords_to_rect(mouse_x, mouse_y)
            print("x: ", new_x, "new_y: ", new_y)

            target_scored(new_x, new_y)

    # Update Pygame display

    pygame.display.update()

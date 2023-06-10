###### _____________ARCHARY PROJECT________________######
# Author List:		[ vidya vepoori, niklesh]
# Filename:			multi_touch_screen.py

import pygame
from pygame.locals import *

class ArcheryPage:

    def __init__(self):
        super(ArcheryPage, self).__init__()

        # intilizing pygame
        pygame.init()

        # Get the dimensions of the user's screen
        screen_info = pygame.display.Info()
        screen_width = screen_info.current_w
        screen_height = screen_info.current_h

        screen_size = (1000, 1000)
        blank_screen = pygame.Surface(screen_size)
        blank_screen.fill((205, 133, 63))

        # text box for exiting the screen
        text_box_width, text_box_height = 200, 30
        text_box_pos = (1700, 1040)
        text_box_rect = pygame.Rect(text_box_pos, (text_box_width, text_box_height))
        input_text = ""


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
        font_size = 30  # replace with your desired font size
        font = pygame.font.Font(None, font_size)

        # text to exit
        label_text = "Type 'exit' to exit"
        label_surface = font.render(label_text, True, (0, 0, 0))
        label_pos = (text_box_rect.x, text_box_rect.y - 30)


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

                white = (255, 254, 255)
                black = (0, 0, 2)

                circle_size = circle_sizes[i]
                circle_color = colors[i]
                circle_position = (target_x, target_y)
                if i == 3:
                    pygame.draw.circle(screen, circle_color,
                                    circle_position, circle_size)
                    pygame.draw.circle(
                        screen, white, circle_position, circle_size+2, 2)
                else:
                    pygame.draw.circle(screen, circle_color,
                                    circle_position, circle_size)
                    pygame.draw.circle(
                        screen, black, circle_position, circle_size+2, 2)
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

            if pixel_color == (205, 133, 63, 255) or pixel_color == (0, 255, 255, 255):  # brown

                # Create text surface with coordinates
                text_color = (0, 100, 0)  # set color
                text(x, y)
                text_surface = font.render(f":(", True, text_color)
                screen.blit(text_surface, (x, y))


        # Wait for the user to close the window
        done = False
        archery_target()

        # main loop
        running = True
        while running:

                for event in pygame.event.get():
                    
                    if event.type == QUIT:
                       running = False
                       # intilizing pygame
        
                    elif event.type == KEYDOWN:
                        if event.key == K_BACKSPACE:
                            input_text = input_text[:-1]  # Remove the last character
                        elif event.key == K_RETURN:
                            if input_text == 'exit':
                                running = False        
                        else:
                            if len(input_text) < 4:
                                input_text += event.unicode

                    elif event.type == pygame.FINGERDOWN:

                        x = int(event.x * 1000)
                        y = int(event.y * 1000)

                        target_scored(x, y)

                        print("x : ", x, "y : ", y)

                    # Clear only the text area
                pygame.draw.rect(screen, (255, 255, 255), text_box_rect)

                # Render the input text
                input_surface = font.render(input_text, True, (0, 0, 0))
                input_rect = input_surface.get_rect()
                input_rect.topleft = (text_box_rect.x + 5, text_box_rect.y + 5)
                screen.blit(input_surface, input_rect)

                # Draw the text box border
                pygame.draw.rect(screen, (0, 0, 0), text_box_rect, 2)
                screen.blit(label_surface, label_pos)

                # Update the text area
                pygame.display.update(text_box_rect)
                pygame.display.update()

        # Quit Pygame
        pygame.quit()
        

        

                
    

        




















import sys

import pygame

textColor = (202, 225, 255)
imgLogo = pygame.image.load("hospitalLogo.png")


class Button:
    def __init__(self, text, width, height, pos,elevation):
        # Core attributes
        self.pressed = False
        self.elevation = elevation
        self.dynamic_elevation = elevation
        self.original_y_pos = pos[1]


        # top rectangle
        self.top_rect = pygame.Rect(pos, (width, height))
        self.top_color = '#6CA6CD'

        # bottom rectangle
        self.bottom_rect = pygame.Rect(pos,(width,elevation))
        self.bottom_color = '#A2B5CD'

        # text in button
        self.text_surf = gui_font.render(text, True, '#FFFFFF')
        self.text_rect = self.text_surf.get_rect(center=self.top_rect.center)

    def draw(self):
        # elevation logic
        self.top_rect.y = self.original_y_pos - self.dynamic_elevation
        self.text_rect.center = self.top_rect.center

        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dynamic_elevation

        pygame.draw.rect(display_surface,self.bottom_color,self.bottom_rect,border_radius = 12)
        pygame.draw.rect(display_surface, self.top_color, self.top_rect, border_radius = 12)
        display_surface.blit(self.text_surf, self.text_rect)
        self.check_click()

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()           # mouse position
        if self.top_rect.collidepoint(mouse_pos):    # check if mouse position is overlapping with topt_rect
            self.top_color = '#6CA6CD'
            if pygame.mouse.get_pressed()[0]:        # if user is pressing button
                self.dynamic_elevation = 0
                self.pressed = True
            else:
                self.dynamic_elevation = self.elevation  # button should jump back if pressing is finished
                if self.pressed == True:
                    print('click')
                    self.pressed == False
        else:
            self.dynamic_elevation = self.elevation
            self.top_color = '#4F94CD'

# Output closes directly, creating an infinite Loop --> while true (always running)
pygame.init()  # Initializse the pygame
display_surface = pygame.display.set_mode((800, 480))  # create the screen (size pixel)
pygame.display.set_caption("PflegeRuf - Krankenhaus Niederrhein")  # Title and Icon (icon in same file)
icon = pygame.image.load('hospital.png')
pygame.display.set_icon(icon)
clock = pygame.time.Clock()
gui_font = pygame.font.Font(None,24)

# button erneut versuchen
button1 = Button('Erneut versuchen', 180, 40, (120, 400),6)
button2 = Button('Weiter',180,40, (500,400),6)

# LOOP FOR RUNNING PYGAME
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    display_surface.fill((16, 79, 139))  # background color
    button1.draw()  # displaying button1
    button2.draw()  # displaying button2

    font = pygame.font.SysFont(None, 24)
    img = font.render('Willkommen im PflegeRuf des Krankenhauses Niederrhein!', True, (202, 225, 255))
    display_surface.blit(img, (170, 20))

    display_surface.blit(imgLogo, (360, 60))

    font = pygame.font.SysFont(None, 30)
    img = font.render('Bitte nutzen Sie die Gesichtserkennung für die Nutzung des PflegeRufs!', True, (202, 225, 255))
    display_surface.blit(img, (40, 150))

    # Update pygame display
    pygame.display.update()
    clock.tick(60)

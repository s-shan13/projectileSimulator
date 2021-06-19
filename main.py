import pygame
import pygame.freetype
from pygame.sprite import Sprite
from enum import Enum
import math
import datetime

pygame.display.set_caption("Projectile Simulator")

#Declaring constants
DARKGRAY = (60,60,60)
WHITE = (255, 255, 255)
RED = (255,0,0)
img1 = pygame.image.load('C:/Users/shant/Projectile.png')
img2 = pygame.image.load('howtouse.png')
clock = pygame.time.Clock()

class animation(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.g1 = []
        self.is_animating = False
        self.animateSlow = False
        self.g1.append(pygame.image.load('gr17.PNG'))
        self.g1.append(pygame.image.load('gr16.PNG'))
        self.g1.append(pygame.image.load('gr15.PNG'))
        self.g1.append(pygame.image.load('gr14.PNG'))
        self.g1.append(pygame.image.load('gr13.PNG'))
        self.g1.append(pygame.image.load('gr12.PNG'))
        self.g1.append(pygame.image.load('gr11.PNG'))
        self.g1.append(pygame.image.load('gr10.PNG'))
        self.g1.append(pygame.image.load('gr9.PNG'))
        self.g1.append(pygame.image.load('gr8.PNG'))
        self.g1.append(pygame.image.load('gr7.PNG'))
        self.g1.append(pygame.image.load('gr6.PNG'))
        self.g1.append(pygame.image.load('gr5.PNG'))
        self.g1.append(pygame.image.load('gr4.PNG'))
        self.g1.append(pygame.image.load('gr3.PNG'))
        self.g1.append(pygame.image.load('gr2.PNG'))
        self.g1.append(pygame.image.load('gr1.PNG'))

        self.current_sprite = 0
        self.image = self.g1[self.current_sprite]

        #Positioning the graph
        self.rect = self.image.get_rect()
        self.rect.topright = [pos_x, pos_y]

    #Subroutine to indicate if it is animating
    def animate(self):
        self.is_animating = True

    #Subroutine to change the image displayed
    def update(self):
        if self.is_animating == True:
            if self.animateSlow == True:
                self.current_sprite += 0.001
            else:
                self.current_sprite += 0.01
            if self.current_sprite >= len(self.g1):
                self.current_sprite = 16
                self.is_animating = False
            self.image = self.g1[int(self.current_sprite)]

class animation2(pygame.sprite.Sprite):  #class for the vertical graph
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.g2 = []
        self.is_animating = False
        self.animateSlow = False

        #Adding images to the list
        self.g2.append(pygame.image.load('graph20.PNG'))
        self.g2.append(pygame.image.load('graph19.PNG'))
        self.g2.append(pygame.image.load('graph18.PNG'))
        self.g2.append(pygame.image.load('graph17.PNG'))
        self.g2.append(pygame.image.load('graph16.PNG'))
        self.g2.append(pygame.image.load('graph15.PNG'))
        self.g2.append(pygame.image.load('graph14.PNG'))
        self.g2.append(pygame.image.load('graph13.PNG'))
        self.g2.append(pygame.image.load('graph12.PNG'))
        self.g2.append(pygame.image.load('graph11.PNG'))
        self.g2.append(pygame.image.load('graph10.PNG'))
        self.g2.append(pygame.image.load('graph9.PNG'))
        self.g2.append(pygame.image.load('graph8.PNG'))
        self.g2.append(pygame.image.load('graph7.PNG'))
        self.g2.append(pygame.image.load('graph6.PNG'))
        self.g2.append(pygame.image.load('graph5.PNG'))
        self.g2.append(pygame.image.load('graph4.PNG'))
        self.g2.append(pygame.image.load('graph3.PNG'))
        self.g2.append(pygame.image.load('graph2.PNG'))
        self.g2.append(pygame.image.load('graph1.PNG'))

        self.current_image = 0
        self.image = self.g2[self.current_image]

        #Positioning the graph
        self.rect = self.image.get_rect()
        self.rect.topright = [pos_x, pos_y]

    #Subroutine to indicate if it is animating
    def animate2(self):
        self.is_animating = True

    #Subroutine to change the image displayed
    def update(self):
        if self.is_animating == True:
            if self.animateSlow == True:
                self.current_image += 0.001
            else:
                self.current_image += 0.01
            if self.current_image >= len(self.g2):
                self.current_image = 19
                self.is_animating = False
            self.image = self.g2[int(self.current_image)]

def create_Surface(text, font_size, text_rgb, bg_rgb):
    """ Returns surface with text written on """
    font = pygame.freetype.SysFont("Courier", font_size, bold=True)
    surface, _ = font.render(text=text, fgcolor=text_rgb, bgcolor=bg_rgb)
    return surface.convert_alpha()

class NewElement(Sprite):
    #An user interface element that can be added to a surface

    def __init__(self, center_position, text, font_size, bg_rgb, text_rgb, action=None):

        self.mouse_over = False  # indicates if the mouse over the element

        # create the default image
        default_image = create_Surface(text=text, font_size=font_size, text_rgb=text_rgb, bg_rgb=bg_rgb)

        # create the image that shows when mouse is over the element
        highlighted_image = create_Surface(text=text, font_size=font_size * 1.2, text_rgb=text_rgb, bg_rgb=bg_rgb)

        # add both images and their rects to lists
        self.images = [default_image, highlighted_image]
        self.rects = [
            default_image.get_rect(center=center_position),
            highlighted_image.get_rect(center=center_position),]
        self.action = action

        # calls the init method of the parent sprite class
        super().__init__()

    # properties that vary the image and its rect when the mouse is over the element
    @property
    def image(self):
        return self.images[1] if self.mouse_over else self.images[0]

    @property
    def rect(self):
        return self.rects[1] if self.mouse_over else self.rects[0]

    def update(self, mouse_pos, mouse_up):
        #mouse_pos tracks the position of the mouse and mouse_up detects when the mouse has been clicked
        if self.rect.collidepoint(mouse_pos):
            self.mouse_over = True
            if mouse_up:
                return self.action
        else:
            self.mouse_over = False

    def draw(self, surface):
        """ Draws element onto a surface """
        surface.blit(self.image, self.rect)

class GameState(Enum):
    #Giving a state value to a variable which will cause a subroutine to run
    QUIT = -1
    TITLE = 0
    NEWWIN = 1
    PRJWIN = 2
    HOWTOUSE = 3
    CALCULATOR = 4
    FIND_DIST = 5
    FINDANGLE = 6
    FINDVEL = 7

def main():
    pygame.init()

    screen = pygame.display.set_mode((1200, 800))
    game_state = GameState.TITLE  #Starts with title on screen

    #Run loop
    while True:
        if game_state == GameState.TITLE:
            game_state = title_screen(screen)
            #If a button is pressed in the title screen it returns a new game state request
        if game_state == GameState.QUIT:
            pygame.quit()
            return
            # Returns a none value. There is nowhere else for the program to go so it end
        if game_state == GameState.NEWWIN:
            game_state = learn(screen)
        # When a button is pressed which changes game state, the learn subroutine is run
        if game_state == GameState.PRJWIN:
            game_state = simulate(screen)

        if game_state == GameState.HOWTOUSE:
            game_state = howToUse(screen)

        if game_state == GameState.CALCULATOR:
            game_state = calculator(screen)

        if game_state == GameState.FIND_DIST:
            game_state = findDist(screen)

        if game_state == GameState.FINDANGLE:
            game_state == findAngle(screen)

        if game_state == GameState.FINDVEL:
            game_state == findVel(screen)
    #More pages and the subroutines that happen on that page can be added by creating game states and assigning the game state to the action of a button


def title_screen(screen):
        #Creating text surfaces
        welcometxt = NewElement(
            center_position=(590,100),
            font_size=30,
            bg_rgb=DARKGRAY,
            text_rgb=WHITE,
            text="WELCOME!"
        )

        learnbtn = NewElement(
            center_position=(590,450),
            font_size=25,
            bg_rgb=DARKGRAY,
            text_rgb=WHITE,
            text="Learn about projectiles",
            action=GameState.NEWWIN
        )

        simbtn = NewElement(
            center_position=(590, 250),
            font_size=25,
            bg_rgb=DARKGRAY,
            text_rgb=WHITE,
            text="Start projecting",
            action=GameState.PRJWIN
        )

        quitbtn = NewElement(
            center_position=(590, 750),
            font_size=15,
            bg_rgb=DARKGRAY,
            text_rgb=WHITE,
            text="Quit",
            action=GameState.QUIT
        )

        usebtn = NewElement(
            center_position=(590, 550),
            font_size=25,
            bg_rgb=DARKGRAY,
            text_rgb=WHITE,
            text="How to use this program",
            action=GameState.HOWTOUSE
        )

        calcButton = NewElement(
            center_position=(590, 350),
            font_size=25,
            bg_rgb=DARKGRAY,
            text_rgb=WHITE,
            text="Projectile Calculator",
            action=GameState.CALCULATOR
        )

        buttons = [learnbtn, quitbtn, simbtn, usebtn, calcButton]
        #stores buttons in a list which makes it easier to perform actions on all the buttons

        while True:  #loop to check if mouse button has been clicked

            screen.fill(DARKGRAY)

            mouse_up = False
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    mouse_up = True
                    #event.button one refers to the primary click of the mouse

            for button in buttons:
                ui_action = button.update(pygame.mouse.get_pos(), mouse_up)
                if ui_action is not None:
                    return ui_action
                # when a button is clicked, the action of the button is returned which returns a change in game state
                button.draw(screen)  #Presents the button in the screen
                welcometxt.draw(screen)
            pygame.display.flip()

def learn(screen):
    returnbtn = NewElement(  #creates a button which takes the user back to the main screen when clicked
        center_position=(590, 750),
        font_size=15,
        bg_rgb=DARKGRAY,
        text_rgb=WHITE,
        text="Go Back",
        action=GameState.TITLE)

    #Run loop
    while True:  # loop to check if mouse button has been clicked
        mouse_up = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
                # event.button one refers to the primary click of the mouse
            screen.fill(DARKGRAY)

        screen.blit(img1, (0, 0))


        ui_action = returnbtn.update(pygame.mouse.get_pos(), mouse_up)
        if ui_action is not None:
            return ui_action
            # when a button is clicked, the action of the button is returned which returns a change in game state
        returnbtn.draw(screen)  #Presents the button in the screen
        pygame.display.flip()


def simulate(screen):
    #Adding text to the screen
    returnbtn = NewElement(
        center_position=(590, 750),
        font_size=15,
        bg_rgb=DARKGRAY,
        text_rgb=WHITE,
        text="Home",
        action=GameState.TITLE
    )

    initialV = NewElement(
        center_position=(40, 25),
        font_size=15,
        bg_rgb=DARKGRAY,
        text_rgb=WHITE,
        text="Speed:",
    )

    Angle = NewElement(
        center_position=(230, 25),
        font_size=15,
        bg_rgb=DARKGRAY,
        text_rgb=WHITE,
        text="Angle:",
    )

    Launch = NewElement(
        center_position=(75, 750),
        font_size=30,
        bg_rgb=RED,
        text_rgb=WHITE,
        text="LAUNCH",
    )

    resetbtn = NewElement(
        center_position=(850, 750),
        font_size=15,
        bg_rgb=DARKGRAY,
        text_rgb=WHITE,
        text="Reset",
    )

    slowbtn = NewElement(
        center_position=(210, 750),
        font_size=15,
        bg_rgb=DARKGRAY,
        text_rgb=WHITE,
        text="Slow down",
    )

    fastbtn = NewElement(
        center_position=(335, 750),
        font_size=15,
        bg_rgb=DARKGRAY,
        text_rgb=WHITE,
        text="Speed up",
    )

    class ball(object):
        def __init__(self, x, y, radius, color):
            self.x = x
            self.y = y
            self.radius = radius
            self.color = color

        #Creating a circle with a black border
        def draw(self, screen):
            pygame.draw.circle(screen, (0, 0, 0), (self.x, self.y), self.radius)
            pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius - 1)

        @staticmethod
        def ballpath(startx, starty, initialSpeed, angle, time):
            velx = math.cos(angle) * initialSpeed
            vely = math.sin(angle) * initialSpeed

            #If speed is too small
            if velx < 20 and vely < 20:
                velx = velx * 5
                vely = vely * 5

            distX = velx * time  # s=ut
            distY = (vely * time) + ((-4.9 * (time) ** 2))  # s=ut+0.5at^2

            newx = round(distX + startx)
            newy = round(starty - distY)  # subtract since the y axis is flipped in pygame

            if newx > 1200:
                newx = newx - 1200

            return (newx, newy)

    base_font = pygame.font.SysFont("Courier", 20)
    #Storing initial speed and velocity
    iVel = '      '
    iAng = '      '

    #Animating the graph for horizontal component
    horizontalGraph = pygame.sprite.Group()
    Animation = animation(850, 10)
    horizontalGraph.add(Animation)

    #Animating graph for vertical component
    verticalGraph = pygame.sprite.Group()
    Animation2 = animation2(1150, 10)
    verticalGraph.add(Animation2)

    active = False
    active2 = False

    #Creating rectangles
    spd1 = pygame.Rect(10,10,140,32)
    ang = pygame.Rect(200, 10, 140, 32)
    lnc = pygame.Rect(15, 735, 120, 32)
    floor = pygame.Rect(0,700,1200,5)
    rst = pygame.Rect(800, 725, 100, 50)
    slow = pygame.Rect(170, 730, 110, 50)
    fast = pygame.Rect(290, 730, 110, 50)

    #Initialising the projectile
    Ball = ball(100, 689, 8, RED)
    x = 0
    y = 0
    time = 0
    initialSpeed = 0
    angle = 0
    shoot = False
    slowDown = False

    #Run loop
    while True:
        screen.fill(DARKGRAY)

        if shoot:
            if Ball.y < 699 - Ball.radius:  # checks of the ball has hit the floor
                if slowDown == True:
                    time +=0.001
                else:
                    time += 0.01
                po = Ball.ballpath(x, y, initialSpeed, angle, time)
                Ball.x = po[0]
                Ball.y = po[1]
            else:
                shoot = False
                Ball.y = 689

            #Displaying the distance travelled
            try:
                dist = "horizontal dist " + str(round(int(float(iVel)) * math.cos(int(float(iAng))) * time, 1))
            except ValueError:
                dist = 0
            hdist = base_font.render(str(dist), True, WHITE, DARKGRAY)
            screen.blit(hdist, [900, 450])

            #Displaying the time taken
            try:
                travelTime = "Time: " + str(round(time,1))
            except ValueError:
                travelTime = 0
            tTime = base_font.render(str(travelTime), True, WHITE, DARKGRAY)
            screen.blit(tTime, [900, 400])

        mouse_up = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
                # event.button one refers to the primary click of the mouse

            #If statement to allow user to type in the box when it is clicked
            if event.type == pygame.MOUSEBUTTONDOWN:
                if ang.collidepoint(event.pos):
                    active2 = True
                    active = False
                if spd1.collidepoint(event.pos):
                    active = True
                    active2 = False
                if lnc.collidepoint(event.pos):

                    if shoot == False:
                        shoot = True
                        x = Ball.x  # Where we are shooting from
                        y = Ball.y
                        time = 0
                        try:
                            initialSpeed = int(float(iVel))
                            angle = (int(float(iAng)) * 2 * math.pi)/360 #Convert angle to radians#
                            Animation.animate()
                            Animation2.animate2()
                        except ValueError:
                            initialSpeed = 0
                            angle = 0

                if rst.collidepoint(event.pos):
                    Ball.x = 100
                    Ball.y = 689
                    Animation.current_sprite = 0
                    Animation2.current_image = 0
                    slowDown = False

                if slow.collidepoint(event.pos):
                    slowDown = True
                    Animation2.animateSlow = True
                    Animation.animateSlow = True

                if fast.collidepoint(event.pos):
                    slowDown = False
                    Animation.animateSlow = False
                    Animation2.animateSlow = False

            # checks if any button is pressed
            if active == True:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        iVel = iVel[0:-1] #deletes the last character
                    else:
                        iVel += event.unicode  #adds the character pressed to the string
            if active2 == True:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        iAng = iAng[0:-1] #deletes the last character
                    else:
                        iAng += event.unicode
            if event.type == pygame.QUIT:
                pygame.quit()

        #Changing the size of a text surface
        ui_action = returnbtn.update(pygame.mouse.get_pos(), mouse_up)
        resetbtn.update(pygame.mouse.get_pos(), mouse_up)
        slowbtn.update(pygame.mouse.get_pos(), mouse_up)
        fastbtn.update(pygame.mouse.get_pos(), mouse_up)
        if ui_action is not None:
            return ui_action


        #Adding a digital clock
        current_time = str(datetime.datetime.now())
        timee = base_font.render(current_time, True, WHITE, DARKGRAY)
        screen.blit(timee, [1006, 740])

        #Drawing text on the screen
        returnbtn.draw(screen)
        initialV.draw((screen))
        Angle.draw(screen)
        Launch.draw(screen)
        resetbtn.draw(screen)
        slowbtn.draw((screen))
        fastbtn.draw(screen)

        #Drawing rectangles on the screen
        pygame.draw.rect(screen, WHITE, ang, 2)
        pygame.draw.rect(screen, WHITE, spd1, 2)
        pygame.draw.rect(screen, WHITE, floor, 3)
        pygame.draw.rect(screen, WHITE, lnc, 3)
        pygame.draw.rect(screen, DARKGRAY, rst, 3)
        pygame.draw.rect(screen, DARKGRAY, slow, 3)
        pygame.draw.rect(screen, DARKGRAY, fast, 3)

        #Drawing objects on the screen
        Ball.draw(screen)
        horizontalGraph.draw(screen)
        verticalGraph.draw(screen)
        
        text_surface = base_font.render(iVel, True, WHITE)
        text2_surface = base_font.render(iAng, True, WHITE)

        screen.blit(text2_surface, (ang.x + 5, ang.y + 5))
        screen.blit(text_surface, (spd1.x + 5, spd1.y + 5)) #The text renders wherever the box is

        pygame.display.update()
        horizontalGraph.update()
        verticalGraph.update()
        pygame.display.flip()

def howToUse(screen):
    #Creating text
    returnbtn = NewElement(
        center_position=(590, 750),
        font_size=15,
        bg_rgb=DARKGRAY,
        text_rgb=WHITE,
        text="Go Back",
        action=GameState.TITLE
    )

    #The run loop
    while True:
        screen.fill(DARKGRAY)
        mouse_up = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
                # event.button one refers to the primary click of the mouse


        screen.blit(img2, (0, 0))

        ui_action = returnbtn.update(pygame.mouse.get_pos(), mouse_up)
        if ui_action is not None:
            return ui_action

        returnbtn.draw(screen)  # Presents the button in the screen
        pygame.display.flip()

def calculator(screen):

    #Creating text
    returnbtn = NewElement(
        center_position=(590, 750),
        font_size=15,
        bg_rgb=DARKGRAY,
        text_rgb=WHITE,
        text="Go Back",
        action=GameState.TITLE
    )

    option1 = NewElement(
        center_position=(590, 200),
        font_size=30,
        bg_rgb=WHITE,
        text_rgb=DARKGRAY,
        text=("Find distance travelled"),
        action=GameState.FIND_DIST
    )

    option2 = NewElement(
        center_position=(590, 400),
        font_size=30,
        bg_rgb=WHITE,
        text_rgb=DARKGRAY,
        text=("Find initial angle"),
        action= GameState.FINDANGLE
    )

    option3 =  NewElement(
        center_position=(590, 600),
        font_size=30,
        bg_rgb=WHITE,
        text_rgb=DARKGRAY,
        text=("Find speed at any point"),
        action= GameState.FINDVEL
    )

    buttons = [returnbtn, option1, option2, option3]

    #Creating rectangles
    opt1Rect = pygame.Rect(0,172, 1200, 60)
    opt2Rect = pygame.Rect(0, 372, 1200, 60)
    opt3Rect = pygame.Rect(0, 572, 1200, 60)


    rectangles = [opt1Rect, opt2Rect, opt3Rect]

    #Run loop
    while True:
        screen.fill(DARKGRAY)

        #Detecting the position of the mouse
        mouse_up = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True

        #Changing size of text when mouse is above it and returning its action if clicked
        for button in buttons:
            ui_action = button.update(pygame.mouse.get_pos(), mouse_up)
            if ui_action is not None:
                return ui_action

        # Drawing rectangles
        for rectangle in rectangles:
            pygame.draw.rect(screen, WHITE, rectangle, 60)

        #Drwawing text on screen
        for button in buttons:
            button.draw(screen)


        pygame.display.flip()

def findDist(screen):

    #Creating text
    returnbtn = NewElement(
        center_position=(590, 750),
        font_size=15,
        bg_rgb=DARKGRAY,
        text_rgb=WHITE,
        text="Go back",
        action=GameState.CALCULATOR
    )

    inp_velocity = NewElement(
        center_position=(160, 40),
        font_size=25,
        bg_rgb=DARKGRAY,
        text_rgb=WHITE,
        text="Initial Velocity: ",
    )

    inp_angle = NewElement(
        center_position=(600, 40),
        font_size=25,
        bg_rgb=DARKGRAY,
        text_rgb=WHITE,
        text="Angle: ",
    )

    inp_height = NewElement(
        center_position=(275, 120),
        font_size=25,
        bg_rgb=DARKGRAY,
        text_rgb=WHITE,
        text="Height relative to the end point: ",
    )

    calc_text = NewElement(
        center_position=(100, 630),
        font_size=35,
        bg_rgb=RED,
        text_rgb=WHITE,
        text="Calculate",
    )

    #List for drawing the text
    texts = [returnbtn, inp_velocity, inp_angle, inp_height, calc_text]

    #Creating rectangles
    inp_velocityRect = pygame.Rect(8, 10, 420, 60)
    inp_angleRect = pygame.Rect(528,10,220,60)
    inp_heightRect = pygame.Rect(8,90,620,60)
    out_calcRect = pygame.Rect(8, 615, 185, 30)

    rectangles = [inp_velocityRect, inp_angleRect, inp_heightRect, out_calcRect]

    #Variables to store input
    varVel = ' '
    varHeight = ' '
    varAngle = ' '

    #Operators to identify which are is being written in
    input1 = False
    input2 = False
    input3 = False
    calculate = False

    #Run loop
    while True:
        screen.fill(DARKGRAY)
        base_font = pygame.font.SysFont("Courier", 20)

        #Calculating the distance
        if calculate:
            vel_y = velocity * math.sin(angle)
            vel_x = velocity * math.cos(angle)
            if height == 0:
                time = vel_y / 4.8
                finalDist = round((vel_x * time),1)
            else:
                time1 = ((-1 * vel_y) - math.sqrt(((vel_y ** 2) - (4 * (-4.9)) * (-1*height))))  # Quadratic formula
                time2 = time1/-9.8
                finalDist = round((vel_x * time2), 1)  # s = ut
            rendered_ans = base_font.render(str(finalDist), True, WHITE, DARKGRAY)
            screen.blit(rendered_ans, (600, 500))

        # Detecting the position of the mouse
        mouse_up = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True

            #Check which rectangle has been clicked and allow user to type
            if event.type == pygame.MOUSEBUTTONDOWN:
                if inp_velocityRect.collidepoint(event.pos):
                    input1 = True
                    input2 = False
                    input3 = False

                if inp_angleRect.collidepoint(event.pos):
                    input1 = False
                    input2 = True
                    input3 = False

                if inp_heightRect.collidepoint(event.pos):
                    input1 = False
                    input2 = False
                    input3 = True

                if out_calcRect.collidepoint(event.pos):
                    try:
                        velocity = int(float(varVel))
                    except ValueError:
                        velocity = 0
                    try:
                        angle = (int(float(varAngle))*2*math.pi)/360  #Convert to radians
                    except ValueError:
                        angle = 0
                    try:
                        height = int(float(varHeight))
                    except ValueError:
                        height = 0
                    calculate = True

            #code to allow user ot type
            if input1 == True:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        varVel = varVel[0:-1] #deletes the last character
                    else:
                        varVel += event.unicode  #adds the character pressed to the string
            if input2 == True:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        varAngle = varAngle[0:-1] #deletes the last character
                    else:
                        varAngle += event.unicode
            if input3 == True:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        varHeight = varHeight[0:-1] #deletes the last character
                    else:
                        varHeight += event.unicode

        # Changing size of text when mouse is above it and returning its action if clicked
        ui_action = returnbtn.update(pygame.mouse.get_pos(), mouse_up)
        if ui_action is not None:
            return ui_action

        #rendering user inputs
        text_surface = base_font.render(varVel, True, WHITE)
        text2_surface = base_font.render(varAngle, True, WHITE)
        text3_surface = base_font.render(varHeight, True, WHITE)

        #Bliting inputs to screen
        screen.blit(text2_surface, (inp_angleRect.x + 115, inp_angleRect.y + 20))
        screen.blit(text_surface, (inp_velocityRect.x + 305, inp_velocityRect.y + 20))
        screen.blit(text3_surface, (inp_heightRect.x + 515, inp_heightRect.y + 20))
        #The text is blit certain amount of pixels away from the top left of the box

        #Drawing text onto screen
        for text in texts:
            text.draw(screen)

        #Drawing rectangles onto screen
        for rectangle in rectangles:
            pygame.draw.rect(screen, WHITE, rectangle, 3)

        pygame.display.flip()

def findAngle(screen):
    # Creating text
    returnbtn = NewElement(
        center_position=(590, 750),
        font_size=15,
        bg_rgb=DARKGRAY,
        text_rgb=WHITE,
        text="Go back",
        action=GameState.CALCULATOR
    )

    inp_velocity = NewElement(
        center_position=(160, 40),
        font_size=25,
        bg_rgb=DARKGRAY,
        text_rgb=WHITE,
        text="Initial Velocity: ",
    )

    inp_dist = NewElement(
        center_position=(170, 120),
        font_size=25,
        bg_rgb=DARKGRAY,
        text_rgb=WHITE,
        text="Distance travelled: ",
    )

    inp_time = NewElement(
        center_position=(555, 40),
        font_size=25,
        bg_rgb=DARKGRAY,
        text_rgb=WHITE,
        text="Time taken: ",
    )

    calc_text = NewElement(
        center_position=(100, 630),
        font_size=35,
        bg_rgb=RED,
        text_rgb=WHITE,
        text="Calculate",
    )

    texts = [returnbtn, inp_velocity, inp_dist, inp_time, calc_text]

    # Creating rectangles
    inp_velocityRect = pygame.Rect(8, 10, 420, 60)
    inp_timeRect = pygame.Rect(450, 10, 320, 60)
    inp_distRect = pygame.Rect(8, 90, 600, 60)
    out_calcRect = pygame.Rect(8, 615, 185, 30)

    rectangles = [inp_velocityRect, inp_distRect, inp_timeRect, out_calcRect]

    # Variables to store input
    varVel = ' '
    vardist = ' '
    vartime = ' '

    # Operators to identify which are is being written in
    input1 = False
    input2 = False
    input3 = False
    calculate = False

    #run loop
    while True:
        screen.fill(DARKGRAY)
        base_font = pygame.font.SysFont("Courier", 20)

        #Calculating the initial angle
        if calculate:
            if time > 0:
                u = distance/time  #Using s = ut
            else:
                u = 0
            if velocity > 0:
                angle_in_rad = math.acos(u/velocity)
                angle_in_degrees = round((angle_in_rad*360)/(2*math.pi), 1)
            else:
                angle_in_degrees = 0
            rendered_ans = base_font.render(str(angle_in_degrees), True, WHITE, DARKGRAY)
            screen.blit(rendered_ans, (600, 500))


        # Detecting the position of the mouse
        mouse_up = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True

            # Check which rectangle has been clicked and allow user to type
            if event.type == pygame.MOUSEBUTTONDOWN:
                if inp_velocityRect.collidepoint(event.pos):
                    input1 = True
                    input2 = False
                    input3 = False

                if inp_timeRect.collidepoint(event.pos):
                    input1 = False
                    input2 = True
                    input3 = False

                if inp_distRect.collidepoint(event.pos):
                    input1 = False
                    input2 = False
                    input3 = True

                if out_calcRect.collidepoint(event.pos):
                    try:
                        velocity = int(float(varVel))
                    except ValueError:
                        velocity = 0
                    try:
                        distance = int(float(vardist))
                    except ValueError:
                        distance = 0
                    try:
                        time = int(float(vartime))
                    except ValueError:
                        time = 0
                    calculate = True

            # code to allow user ot type
            if input1 == True:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        varVel = varVel[0:-1]  # deletes the last character
                    else:
                        varVel += event.unicode  # adds the character pressed to the string
            if input2 == True:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        vartime = vartime[0:-1]  # deletes the last character
                    else:
                        vartime += event.unicode
            if input3 == True:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        vardist = vardist[0:-1]  # deletes the last character
                    else:
                        vardist += event.unicode

        # Changing size of text when mouse is above it and returning its action if clicked
        ui_action = returnbtn.update(pygame.mouse.get_pos(), mouse_up)
        if ui_action is not None:
            return ui_action

        # rendering user inputs
        text_surface = base_font.render(varVel, True, WHITE)
        text2_surface = base_font.render(vartime, True, WHITE)
        text3_surface = base_font.render(vardist, True, WHITE)

        # Bliting inputs to screen
        screen.blit(text2_surface, (inp_timeRect.x + 220, inp_timeRect.y + 20))
        screen.blit(text_surface, (inp_velocityRect.x + 305, inp_velocityRect.y + 20))
        screen.blit(text3_surface, (inp_distRect.x + 400, inp_distRect.y + 20))
        # The text is blit certain amount of pixels away from the top left of the box

        # Drawing text onto screen
        for text in texts:
            text.draw(screen)

        # Drawing rectangles onto screen
        for rectangle in rectangles:
            pygame.draw.rect(screen, WHITE, rectangle, 3)

        pygame.display.flip()

def findVel(screen):
    # Creating text
    returnbtn = NewElement(
        center_position=(590, 750),
        font_size=15,
        bg_rgb=DARKGRAY,
        text_rgb=WHITE,
        text="Go back",
        action=GameState.CALCULATOR
    )

    inp_velocity = NewElement(
        center_position=(160, 40),
        font_size=25,
        bg_rgb=DARKGRAY,
        text_rgb=WHITE,
        text="Initial Velocity: ",
    )

    inp_angle = NewElement(
        center_position=(600, 40),
        font_size=25,
        bg_rgb=DARKGRAY,
        text_rgb=WHITE,
        text="Angle: ",
    )

    inp_distance = NewElement(
        center_position=(275, 120),
        font_size=25,
        bg_rgb=DARKGRAY,
        text_rgb=WHITE,
        text="Distance travelled (horizontal): ",
    )

    calc_text = NewElement(
        center_position=(100, 630),
        font_size=35,
        bg_rgb=RED,
        text_rgb=WHITE,
        text="Calculate",
    )

    # List for drawing the text
    texts = [returnbtn, inp_velocity, inp_angle, inp_distance, calc_text]

    # Creating rectangles
    inp_velocityRect = pygame.Rect(8, 10, 420, 60)
    inp_angleRect = pygame.Rect(528, 10, 220, 60)
    inp_distRect = pygame.Rect(8, 90, 620, 60)
    out_calcRect = pygame.Rect(8, 615, 185, 30)

    rectangles = [inp_velocityRect, inp_angleRect, inp_distRect, out_calcRect]

    # Variables to store input
    varVel = ' '
    vardist = ' '
    varAngle = ' '

    # Operators to identify which are is being written in
    input1 = False
    input2 = False
    input3 = False
    calculate = False

    # Run loop
    while True:
        screen.fill(DARKGRAY)
        base_font = pygame.font.SysFont("Courier", 20)

        # Calculating the distance
        if calculate:
            initial_vertical = velocity*math.sin(angle)
            horizontal_vel = velocity*math.cos(angle)
            vertical_velocity = math.sqrt(math.sqrt(((initial_vertical**2) + 2*(-9.8)*distance)**2)) #using v^2 = u^2 + 2as
            final_speed =round( math.sqrt((vertical_velocity**2)+(horizontal_vel**2)), 1)  #using pythagoras' theorum
            rendered_ans = base_font.render(str(final_speed), True, WHITE, DARKGRAY)
            screen.blit(rendered_ans, (600, 500))

        # Detecting the position of the mouse
        mouse_up = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True

            # Check which rectangle has been clicked and allow user to type
            if event.type == pygame.MOUSEBUTTONDOWN:
                if inp_velocityRect.collidepoint(event.pos):
                    input1 = True
                    input2 = False
                    input3 = False

                if inp_angleRect.collidepoint(event.pos):
                    input1 = False
                    input2 = True
                    input3 = False

                if inp_distRect.collidepoint(event.pos):
                    input1 = False
                    input2 = False
                    input3 = True

                if out_calcRect.collidepoint(event.pos):
                    try:
                        velocity = int(float(varVel))
                    except ValueError:
                        velocity = 0
                    try:
                        angle = (int(float(varAngle)) * 2 * math.pi) / 360  # Convert to radians
                    except ValueError:
                        angle = 0
                    try:
                        distance = int(float(vardist))
                    except ValueError:
                        distance = 0
                    calculate = True

            # code to allow user ot type
            if input1 == True:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        varVel = varVel[0:-1]  # deletes the last character
                    else:
                        varVel += event.unicode  # adds the character pressed to the string
            if input2 == True:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        varAngle = varAngle[0:-1]  # deletes the last character
                    else:
                        varAngle += event.unicode
            if input3 == True:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        vardist = vardist[0:-1]  # deletes the last character
                    else:
                        vardist += event.unicode

        # Changing size of text when mouse is above it and returning its action if clicked
        ui_action = returnbtn.update(pygame.mouse.get_pos(), mouse_up)
        if ui_action is not None:
            return ui_action

        # rendering user inputs
        text_surface = base_font.render(varVel, True, WHITE)
        text2_surface = base_font.render(varAngle, True, WHITE)
        text3_surface = base_font.render(vardist, True, WHITE)

        # Bliting inputs to screen
        screen.blit(text2_surface, (inp_angleRect.x + 115, inp_angleRect.y + 20))
        screen.blit(text_surface, (inp_velocityRect.x + 305, inp_velocityRect.y + 20))
        screen.blit(text3_surface, (inp_distRect.x + 515, inp_distRect.y + 20))
        # The text is blit certain amount of pixels away from the top left of the box

        # Drawing text onto screen
        for text in texts:
            text.draw(screen)

        # Drawing rectangles onto screen
        for rectangle in rectangles:
            pygame.draw.rect(screen, WHITE, rectangle, 3)

        pygame.display.flip()

# call main when the script is run
if __name__ == "__main__":
    main()  
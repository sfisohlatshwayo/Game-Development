import pygame
import time
import random


#initialize pygame always
pygame.init()

display_width = 800
display_height = 600
car_width = 100

#define colors
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

#create a  frame with width and height
gameDisplay = pygame.display.set_mode((display_width,display_height))

#name the frane
pygame.display.set_caption('SA Race')

#define a clock for the game
clock = pygame.time.Clock()

#load the image of a car
carImg = pygame.image.load('carImage.png')
#block moving towards the car
def things(thingx,thingy,thingw,thingh,color):
    
    pygame.draw.rect(gameDisplay,color,[thingx,thingy,thingw,thingh])

def car(x,y):
    #draw the image in the background
    gameDisplay.blit(carImg,(x,y))

def crash():
    message_display('You Crashed')

def text_objects(text,font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text,largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)
    gameLoop()
    


def gameLoop():
    #determine the location of the image
    x = (display_width*0.45)
    y = (display_height*0.7)

    x_change = 0
    thing_startx =random.randrange(0,display_width)
    thing_starty =-600
    thing_speed = 7
    thing_width =100 
    thing_height =100
    #y_change = 0
        
    gameExit = False

    #while  we are not game Exit 
    while not gameExit:

        #getting all event in game
        for event in pygame.event.get():
            #if the user want to quit
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
                #elif event.key == pygame.K_MINUS:
                    #y_change = -10
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
            
        #adding the value of x _change to location of the frame
        x += x_change
        #y += y_change           
                
            #print all the events happening 
        #print(event)
        gameDisplay.fill(white)
        #things(thingx,thingy,thingw,thingh,color)
        things(thing_startx,thing_starty,thing_width,thing_height,black)
        thing_starty+=thing_speed 
        
        car(x,y)
        
        #Adding Boundaries at the edge  of wall frame
        if x > display_width - car_width or x<0:
            crash()
        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0,display_width-thing_width)
        #if  block crossing of the car
        if y < thing_starty + thing_height:
            print('y crossing over')
            if x > thing_startx and x < thing_startx + thing_width or x + car_width > thing_startx and x + car_width < thing_startx + thing_width:
                print('y crossing over')
                crash()
                
        
        #update the screen/frame
        pygame.display.update()
        #update the frame per second
        clock.tick(60)

gameLoop()
#quite pygame same as initilizing
pygame.quit()

quit()



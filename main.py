
import pygame 
import sys 
import random

jokes = [
    "Dear Math, grow up and solve your own problems",
    "What do you call a factory that makes okay products? A satisfactory.",
    "I only know 25 letters of the alphabet, I don't know y",
    "What did the ocean say to the beach? Nothing, it just waved.",
    "What's the best thing about Switzerland? I don't know, but the flag is a big plus.",
    "What has more letters than the alphabet? The post office!",
    "I don't trust stairs. They're always up to something.",
    "Why can't a nose be 12 inches long? Because then it would be a foot."
]

  
# initializing the constructor 
pygame.init() 
  
# screen resolution 
res = (2500,130) 
  
# opens up a window 
screen = pygame.display.set_mode(res) 

imp = pygame.image.load("C:\\Users\\OrduluGandalf\\Downloads\\Png (2).png").convert()
  
# white color 
color = (255,255,255) 
  
# light shade of the button 
color_light = (170,170,170) 
  
# dark shade of the button 
color_dark = (100,100,100) 
  
# stores the width of the 
# screen into a variable 
width = screen.get_width() 
  
# stores the height of the 
# screen into a variable 
height = screen.get_height() 
  
# defining a font 
smallfont = pygame.font.SysFont('Corbel',30) 
  
# rendering a text written in 
# this font 
text = smallfont.render(' move the window to your and click the first word' , True , color) 
  
while True: 
      
    for ev in pygame.event.get(): 
          
        if ev.type == pygame.QUIT: 
            text = smallfont.render('no' , True , color)  
              
        #checks if a mouse is clicked 
        if ev.type == pygame.MOUSEBUTTONDOWN: 
              
            #if the mouse is clicked on the 
            # button the game is terminated 
            if width/123 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40: 
                text = smallfont.render(random.choice(jokes), True , color) 
                   
    # fills the screen with a color 
    screen.fill((240,25,60)) 
      
    # stores the (x,y) coordinates into 
    # the variable as a tuple 
    mouse = pygame.mouse.get_pos() 
      
    # if mouse is hovered on a button it 
    # changes to lighter shade  
    if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40: 
        a = pygame.draw.rect(screen,color_light,[width/1,height/2,140,40]) 
          
    else: 
        a = pygame.draw.rect(screen,color_dark,[width/1,height/2,140,40]) 
      
    # superimposing the text onto our button 
    screen.blit(text , (width/2+50,height/2)) 
      
    # updates the frames of the game 
    pygame.display.update() 


import subprocess
import pygame
from pygame.locals import *
import os
import main



# Game Initialization
pygame.init()
 
# Center the Game Application
os.environ['SDL_VIDEO_CENTERED'] = '1'
 
# Game Resolution
screen_width=1024
screen_height=600
screen=pygame.display.set_mode((screen_width, screen_height))
 
# Text Renderer
def text_format(message, textFont, textSize, textColor):
    newFont=pygame.font.Font(textFont, textSize)
    newText=newFont.render(message, 0, textColor)
 
    return newText
 
 
# Colors
white=(255, 255, 255)
black=(0, 0, 0)
gray=(50, 50, 50)
red=(255, 0, 0)
green=(0, 255, 0)
blue=(0, 0, 255)
yellow=(255, 255, 0)
 
# Game Fonts
font = "Pixeled.ttf"
 
# Sounds
select_sound = pygame.mixer.Sound("pong2.wav")

# Game Framerate
clock = pygame.time.Clock()
FPS=30

# Main Menu
def main_menu():
 
    menu=True
    selected="start"
 
    while menu:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                pygame.mixer.Sound.play(select_sound)
                if event.key==pygame.K_UP:
                    selected="start"
                elif event.key==pygame.K_DOWN:
                    selected="quit"
                if event.key==pygame.K_RETURN:
                    if selected=="start":
                        level_select()
                    if selected=="quit":
                        pygame.quit()
                        quit()
 
        # Main Menu UI
        screen.fill(black)
        title=text_format("PiG-C PONG", font, 45, white)
        if selected=="start":
            text_start=text_format("START", font, 35, white)
        else:
            text_start = text_format("START", font, 35, gray)
        if selected=="quit":
            text_quit=text_format("QUIT", font, 35, white)
        else:
            text_quit = text_format("QUIT", font, 35, gray)
 
        title_rect=title.get_rect()
        start_rect=text_start.get_rect()
        quit_rect=text_quit.get_rect()
 
        # Main Menu Text
        screen.blit(title, (screen_width/2 - (title_rect[2]/2), 80))
        screen.blit(text_start, (screen_width/2 - (start_rect[2]/2), 300))
        screen.blit(text_quit, (screen_width/2 - (quit_rect[2]/2), 360))
        pygame.display.update()
        clock.tick(FPS)
        pygame.display.set_caption("PiG-C Pong Main Menu")


def level_select():
    menu=True
    selection=["easy", "medium", "hard", "unfair"]
    s: int =0
    selected = selection[s]
    
    while menu:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                pygame.mixer.Sound.play(select_sound)
                if event.key==pygame.K_UP:
                    s-=1
                    if(s<0):
                        s=3
                    selected=selection[s]
                    print(selected)
                elif event.key==pygame.K_DOWN:
                    s+=1
                    if (s>3):
                        s=0
                    selected=selection[s]
                    print(selected)
                if event.key==pygame.K_RETURN:
                    if selected=="easy":
                        print("Start")
                        main.easyLoop()
                    if selected=="medium":
                        print("Coming soon")
                    if selected=="hard":
                        print("Coming soon")
                    if selected=="unfair":
                        print("Coming soon")
                    
 
        # Main Menu UI
        screen.fill(black)
        title=text_format("LEVEL SELECT", font, 45, white)
        if selected=="easy":
            text_easy=text_format("easy", font, 35, white)
        else:
            text_easy = text_format("easy", font, 35, gray)
        if selected=="medium":
            text_med=text_format("medium", font, 35, white)
        else:
            text_med = text_format("medium", font, 35, gray)
        if selected=="hard":
            text_hard=text_format("hard", font, 35, white)
        else:
            text_hard = text_format("hard", font, 35, gray)
        if selected=="unfair":
            text_unf=text_format("unfair", font, 35, white)
        else:
            text_unf = text_format("unfair", font, 35, gray)
 
        title_rect=title.get_rect()
        easy_rect=text_easy.get_rect()
        med_rect=text_med.get_rect()
        hard_rect=text_hard.get_rect()
        unf_rect=text_unf.get_rect()
 
        # Main Menu Text
        screen.blit(title, (screen_width/2 - (title_rect[2]/2), 50))
        screen.blit(text_easy, (screen_width/2 - (easy_rect[2]/2), 200))
        screen.blit(text_med, (screen_width/2 - (med_rect[2]/2), 260))
        screen.blit(text_hard, (screen_width/2 - (hard_rect[2]/2), 320))
        screen.blit(text_unf, (screen_width/2 - (unf_rect[2]/2), 380))
        pygame.display.update()
        clock.tick(FPS)
        pygame.display.set_caption("PiG-C Pong Main Menu")

main_menu()
pygame.quit()
quit()
#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys, pygame
from pygame.locals import *
import datetime
from subprocess import *

class CenteredText(object):
    """ Centered Text Class
    """
    def __init__(self, text, font, (x,y,w,h), color=(0,0,0)):
        self.x, self.y, self.w, self.h = x,y,w,h
        pygame.font.init()
        width, height = font.size(text)
        xoffset = (self.w-width) // 2
        yoffset = (self.h-height) // 2
        self.coords = self.x+xoffset, self.y+yoffset
        self.txt = font.render(text, True, color)

    def draw(self, screen):
        screen.blit(self.txt, self.coords)
        # for testing purposes, draw the rectangle too
        #rect = Rect(self.x, self.y, self.w, self.h)
        #pygame.draw.rect(screen, (255,0,0), rect, 1)

if __name__ == '__main__': 
    size = width, height = 1680, 1050
    
    print "Starting pygame..."

    screen = pygame.display.set_mode(size, pygame.FULLSCREEN)

    pygame.init()

    background = 0, 0, 0
    foreground = 255, 255, 255
    red = 255, 0, 0

    dayFont = pygame.font.SysFont("sans", 192)
    timeOfDayFont = pygame.font.SysFont("sans", 128)
    clockFont = pygame.font.SysFont("sans", 300)
    dateFont = pygame.font.SysFont("sans", 128)

    fpsClock = pygame.time.Clock()

    while 1:

        for event in pygame.event.get():
            if event.type == QUIT:
               sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit(0)

        screen.fill(background)

        d = datetime.datetime.now()

        weekday = d.strftime("%A")
        clock = d.strftime("%I:%M %p")
        clock = clock.lstrip("0").lower()
        date = d.strftime("%B %d, %Y")
        
        hour = int(d.strftime("%H"))
        if(hour < 6):
            timeOfDay = "Night"
        elif(hour < 12):
            timeOfDay = "Morning"
        elif(hour < 13):
            timeOfDay = "Noon"
        elif(hour < 17):
            timeOfDay = "Afternoon"
        elif(hour < 20):
            timeOfDay = "Evening"
        else:
            timeOfDay = "Night"

        dayText = CenteredText(weekday, dayFont, (0, 50, 1680, 200), foreground)
        dayText.draw(screen)

        timeOfDayText = CenteredText(timeOfDay, timeOfDayFont, (0, 300, 1680, 100), foreground)
        timeOfDayText.draw(screen)

        clockText = CenteredText(clock, clockFont, (0, 450, 1680, 400), foreground)
        clockText.draw(screen)

        dateText = CenteredText(date, dateFont, (0, 850, 1680, 150), foreground)
        dateText.draw(screen)

        pygame.display.update() 
        fpsClock.tick(5)  

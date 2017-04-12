#!/usr/bin/python3
# encoding=utf-8

"""
                         _____  _____  _____  _____  _____         _____
           /////  /     /____/ /___ / /___ / /_ __/ /_ __/ /|  // /____/
           ////  //    //___  //__// //__//   //     //   / | // //___
          ////  //    // \ / / ___/ /___ /   //     //   //||// // \ /
          ///  ///   //__// //\\   //  //   //   __//_  // | / //__//
         ///  ///   /____/ //  \\ //  //   //   /____/ //  |/ /____/
         //  ////      _   _   _   _   _  _ _  _   _  _ _  __  __
        //  ////  |   |_| |_) / \ |_) |_|  |  / \ |_)  |  |_  (_
        /  /////  |__ | | |_) \_/ | \ | |  |  \_/ | \ _|_ |__ __)
    =================================================================
      Use <UP> and <DOWN> to choose a line.  Use <LEFT> and <RIGHT>
      to move it around.  Use <ESC> to quit.
"""

import pygame
from pygame.locals import *

pygame.init()
pygame.display.set_mode((1920, 1080), FULLSCREEN)
SURFACE = pygame.display.get_surface()
FONT = pygame.font.Font('font/wqy-microhei.ttc', 48)
FPS = 60

XS = [970, 980, 990, 1000, 1010, 1020, 1030]
INDEX = 3
running = True

clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == KEYUP:
            if event.key == K_LEFT:
                XS[INDEX] = max(0, XS[INDEX] - 1)
            elif event.key == K_RIGHT:
                XS[INDEX] = min(1919, XS[INDEX] + 1)
            elif event.key == K_UP:
                INDEX = min(6, INDEX + 1)
            elif event.key == K_DOWN:
                INDEX = max(0, INDEX - 1)
            elif event.key == K_ESCAPE:
                running = False
    SURFACE.fill(0)
    for i in range(7):
        pygame.draw.line(SURFACE, 0x00ff00, (XS[i], 0), (XS[i], 1079))
    text = FONT.render('XS: ' + ', '.join(map(str, XS)), True, (0, 0, 255))
    rect = text.get_rect()
    rect.topleft = (0, 0)
    SURFACE.blit(text, rect)
    pygame.display.flip()
    clock.tick(FPS)

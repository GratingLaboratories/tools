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
      Use <UP>  and <DOWN>  to adjust  the step.    Use <LEFT>  and
      <RIGHT>  to change  the PPL  (pixels per line).    Use  <ESC>
      to quit.
"""

import pygame
from pygame.locals import *

pygame.init()
pygame.display.set_mode((1920, 1080), FULLSCREEN)
SURFACE = pygame.display.get_surface()
FONT = pygame.font.Font('font/wqy-microhei.ttc', 48)
FPS = 60

PPL = 2  # pixels per line
STEP = 0.1
blue = False
running = True

clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == KEYUP:
            if event.key == K_LEFT:
                PPL = max(1, PPL - STEP)
            elif event.key == K_RIGHT:
                PPL += STEP
            elif event.key == K_UP:
                STEP *= 10
            elif event.key == K_DOWN:
                STEP *= 0.1
            elif event.key == K_b:
                blue = not blue
            elif event.key == K_ESCAPE:
                running = False
    SURFACE.fill(0)
    x = 0.0
    while x < 1910.0:
        pygame.draw.line(SURFACE, 0x00ff00, (int(x), 0), (int(x), 1079))
        if blue:
            pygame.draw.line(SURFACE, 0x0000ff, (int(x)+1, 0), (int(x)+1, 1079))
        x += PPL
    text = FONT.render('PPL: %g | step: %g' % (PPL, STEP), True, (0, 0, 255))
    rect = text.get_rect()
    rect.topleft = (0, 0)
    SURFACE.blit(text, rect)
    pygame.display.flip()
    clock.tick(FPS)

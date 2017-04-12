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
      Use <Q>, <W>, <E>, <R>, <T> and <Y> to flip each column's red
      component.   Use <A>, <S>, <D>, <F>, <G> and <H> to flip each
      column's  green component.   Use <Z>, <X>, <C>, <V>, <B>  and
      <N> to flip each column's blue component.  Use <ESC> to quit.
"""

import pygame
from pygame.locals import *

pygame.init()
pygame.display.set_mode((1920, 1080), FULLSCREEN)
SURFACE = pygame.display.get_surface()
FONT = pygame.font.Font('font/wqy-microhei.ttc', 48)
FPS = 60

keymap = [
    [],  # reserved for Fn
    [],  # reserved for numbers
    [K_q, K_w, K_e, K_r, K_t, K_y],
    [K_a, K_s, K_d, K_f, K_g, K_h],
    [K_z, K_x, K_c, K_v, K_b, K_n]]
keys = {}
for i in range(len(keymap)):
    for j in range(len(keymap[i])):
        keys[keymap[i][j]] = i, j
colors = [0] * 6
running = True

clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                running = False
            if event.key in keys:
                x, y = keys[event.key]
                if x in range(2, 5) and y in range(6):
                    colors[y] ^= 0xff << ((4 - x) * 8)
    SURFACE.fill(0)
    x = 0.0
    while x < 1910.0:
        for i in range(6):
            pygame.draw.line(SURFACE, colors[i], (int(x)+i, 0), (int(x)+i, 1079))
        x += 6.11
    text = FONT.render('colors: ' + ', '.join(map(hex, colors)), True, (128, 128, 128))
    rect = text.get_rect()
    rect.topleft = (0, 0)
    SURFACE.blit(text, rect)
    pygame.display.flip()
    clock.tick(FPS)

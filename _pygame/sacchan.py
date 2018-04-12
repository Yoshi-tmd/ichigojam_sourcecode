""" sacchan.py """
import sys
import pygame
from pygame.locals import *
import random

WIDTH = 640
HEIGHT = 480

pygame.init()
surface = pygame.display.set_mode((WIDTH, HEIGHT))
fpslock = pygame.time.Clock()

# main routine function
def main():
    # initial rope status
    first_ropepos_x = random.randint(0, 2)
    if first_ropepos_x == 0:
        rppos_x = WIDTH * 0.1
        rope_velocity = 8
    else:
        rppos_x = WIDTH * 0.9
        rope_velocity = -8
    rope_accel = 0.8
    rppos_y = HEIGHT * 0.9

    # initial sacchan status
    scpos_x = WIDTH / 2
    scpos_y = HEIGHT * 0.9
    sc_velovity = 99
    sc_accel = 1

    score = 0

    font = pygame.font.SysFont(None,20)

    running = True
    # while loop
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDWON:
                if event.type == K_SPACE:
                    sc_velovity = -100

        surface.fill((0, 0, 0))

        # move sacchan
        if sc_velovity != 99:
            scpos_y += sc_velovity
            sc_velovity += sc_accel

        # get score
        if scpos_y > HEIGHT * 0.9:
            sc_velovity = 99
            score += 1

        # move rope
        rppos_x += rope_velocity
        if rppos_x > WIDTH / 2:
            rope_velocity -= rope_accel
        elif rppos_x < WIDTH / 2:
            rope_velocity += rope_accel

        # draw object
        pygame.draw.rect(surface, (255, 255, 255), Rect(rppos_x, rppos_y, 20, 10))
        pygame.draw.rect(surface, (255, 255, 0), Rect(scpos_x, scpos_y, 30, 40))

        # draw score
        # rend_score = font.render(str(score), True, (255, 255, 255))
        # surface.blit(rend_score, (WIDTH * 0.9, HEIGHT * 0.1))

        pygame.display.update()
        fpslock.tick(60)

if __name__ == '__main__':
    main()

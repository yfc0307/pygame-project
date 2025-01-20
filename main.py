# Code by Chen Yufan
# Version 1

import pygame, sys
from setting import *
from level import Level
from player import Player

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.set_caption('Math World Adventure')
        self.clock = pygame.time.Clock()
        self.level = Level()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            dt = self.clock.tick() / 1000
            self.level.run(dt)
            print(dt)
            pygame.display.update()

    def createText(self,font,text,color,pos,size):
        self.text_font = pygame.font.Font(font, size)
        self.surface = self.text_font.render(text, True, color)
        self.text_rect = self.surface.get_rect(center=pos)

if __name__ == '__main__':
    game = Game()
    game.run()
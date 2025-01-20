import pygame
from setting import *
from sys import exit
import os
from support import *
from timer import *

class Player(pygame.sprite.Sprite): 
    # Remember to call player = pygame.sprite.GroupSingle()
    # player.add(Player())
    # in main function
    def __init__(self, pos, group):
        super().__init__(group)

        self.import_assets()
        self.status = 'player_r'
        self.player_index = 0
        self.frame_index = 0

        self.image = self.animations[self.status][self.player_index]
        self.rect = self.image.get_rect(center=pos)
        self.speed = 400

        # Deter the direction, for example (1,0) is going right
        self.direction = pygame.math.Vector2()
        # The position of player
        self.pos = pygame.math.Vector2(self.rect.center)

        self.player_stat = {
            'maze_key': 0, # 0 for not equipped, 1 for equipped
            'maze_ez': 0, # 0 for not cleared, 1 for cleared
            'maze_hd': 0,
            'quiz_key': 0, 
            'quiz_ez': 0,
            'quiz_hd': 0,
        }

        self.quiz_clear = False
        self.maze_clear = False
        self.boss_clear = False

        self.player_score = {
            'maze_ez_score': 0,
            'maze_hd_score': 0,
            'quiz_ez_score': 0,
            'quiz_hd_score': 0,
        }

    def clear(self, index):
        if index == 0:
            self.quiz_clear = True
        elif index == 1:
            self.maze_clear = True
        elif index == 2:
            self.boss_clear = True
        elif index == -1:
            self.quiz_clear = False
            self.maze_clear = False
            self.boss_clear = False

    def refresh_pos(self):
        self.status = 'player_r'
        self.player_index = 0
        self.frame_index = 0
        self.pos = (500,400)
        

    def refresh_stat(self):
        self.speed = 400
        self.player_stat = {
            'maze_key': 0, # 0 for not equipped, 1 for equipped
            'maze_ez': 0, # 0 for not cleared, 1 for cleared
            'maze_hd': 0,
            'quiz_key': 0, 
            'quiz_ez': 0,
            'quiz_hd': 0,
        }

        self.player_score = {
            'maze_ez_score': 0,
            'maze_hd_score': 0,
            'quiz_ez_score': 0,
            'quiz_hd_score': 0,
        }

        self.quiz_clear = False
        self.maze_clear = False
        self.boss_clear = False

    def import_assets(self):

        # REMEMBER TO ADD folder name of newly added animation images in self.animations

        self.animations = {'player_d': [], 'player_l': [], 'player_r': [],'player_u': [],
                           'player_d_idle': [],'player_l_idle': [],'player_r_idle': [],'player_u_idle': []}

        for animation in self.animations.keys():
            full_path = os.path.join(os.path.dirname(__file__),'texture','player',animation)
            self.animations[animation] = import_folder(full_path) # This function is inside support.py
        print(self.animations)

    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.direction.x = -1
            self.status = 'player_l'
        elif keys[pygame.K_d]:
            self.direction.x = 1
            self.status = 'player_r'
        else:
            self.direction.x = 0
        if keys[pygame.K_w]:
            self.direction.y = -1
            self.status = 'player_u'
        elif keys[pygame.K_s]:
            self.direction.y = 1
            self.status = 'player_d'
        else:
            self.direction.y = 0


    def move(self,dt):
        if self.direction.magnitude() > 0: 
            self.direction = self.direction.normalize()

        self.image = self.animations[self.status][self.player_index]
        self.pos += self.direction * self.speed * dt
        self.rect.center = self.pos

    def anim(self,dt):
        self.frame_index += 4 * dt
        if self.frame_index >= len(self.animations[self.status]):
            self.frame_index = 0
        self.image = self.animations[self.status][int(self.frame_index)]

    def get_status(self):

        # idle
        if self.direction.magnitude() == 0: # This means the player stops moving at any direction
            self.status = self.status.split('_')[0] + '_' + self.status.split('_')[1] + '_idle'
        
    def update(self, dt):
        self.input()
        self.move(dt)
        self.get_status()
        self.anim(dt)

import pygame, os, time
from setting import *
from player import Player
from support import *
from maze import Maze
from quiz import QuickMathGame

class Level:
    def __init__(self):
        self.screen = pygame.display.get_surface()

        self.off_screen = pygame.Surface((1600,1400))

        self.all_sprites = PlayerGroup()

        self.import_map_imgs()

        self.create_edges()

        self.world_edge = False

        self.prev_index = 0 # Store the map index of player previously switched from (Please note that menu switch also counts)
        self.map_index = 0 # Store the map index of player currently in. REMEMBER THIS SHOULD START FROM 0 so game can start from menu
        self.menu_index = 0
        self.timeline = 0 # This determines the progress of storyline
        self.spawn = (500,400) # Default spawn in middle

        self.quiz_highscore = 0
        self.maze_highscore = 0


        
        self.setup()

        self.popup_color = pygame.Color(255,255,255)
        self.fog_alpha = 0

        self.showmaze = True # True when maze interface
        self.maze_refresh = True # Default True to activate first maze
        self.load_wall_point = True # Default True to activate wall point
        self.refresh_quiz = True
        self.input_text = '' # For math quiz text input
        self.answer = -1 # For math quiz submitted answer
        self.timer = True # For math quiz

        self.showmsg = False
        self.currenttext = "This should be the message."

    def import_map_imgs(self):
        self.floor1 = pygame.image.load(os.path.join(os.path.dirname(__file__),'texture','1_floor.png')).convert_alpha()
        self.floor2 = pygame.image.load(os.path.join(os.path.dirname(__file__),'texture','2_floor.png')).convert_alpha()
        self.floor3 = pygame.image.load(os.path.join(os.path.dirname(__file__),'texture','3_floor.png')).convert_alpha()
        self.floor4 = pygame.image.load(os.path.join(os.path.dirname(__file__),'texture','4_floor.png')).convert_alpha()
        self.floor5 = pygame.image.load(os.path.join(os.path.dirname(__file__),'texture','5_floor.png')).convert_alpha()
        self.floor6 = pygame.image.load(os.path.join(os.path.dirname(__file__),'texture','6_floor.png')).convert_alpha()
        self.floor7 = pygame.image.load(os.path.join(os.path.dirname(__file__),'texture','7_floor.png')).convert_alpha()
        self.floor8 = pygame.image.load(os.path.join(os.path.dirname(__file__),'texture','8_floor.png')).convert_alpha()
        self.floor9 = pygame.image.load(os.path.join(os.path.dirname(__file__),'texture','9_floor.png')).convert_alpha()
        self.floor10 = pygame.image.load(os.path.join(os.path.dirname(__file__),'texture','10_floor.png')).convert_alpha()
        self.floor11 = pygame.image.load(os.path.join(os.path.dirname(__file__),'texture','11_floor.png')).convert_alpha()
        self.floor12 = pygame.image.load(os.path.join(os.path.dirname(__file__),'texture','12_floor.png')).convert_alpha()
        self.floor13 = pygame.image.load(os.path.join(os.path.dirname(__file__),'texture','13_floor.png')).convert_alpha()
        self.floor14 = pygame.image.load(os.path.join(os.path.dirname(__file__),'texture','14_floor.png')).convert_alpha()
        self.floor15 = pygame.image.load(os.path.join(os.path.dirname(__file__),'texture','15_floor.png')).convert_alpha()
        self.floor16 = pygame.image.load(os.path.join(os.path.dirname(__file__),'texture','16_floor.png')).convert_alpha()

        self.floor17 = pygame.image.load(os.path.join(os.path.dirname(__file__),'texture','17_floor.png')).convert_alpha()
        self.floor19 = pygame.image.load(os.path.join(os.path.dirname(__file__),'texture','19_floor.png')).convert_alpha()
        self.floor21 = pygame.image.load(os.path.join(os.path.dirname(__file__),'texture','21_floor.png')).convert_alpha()
        self.floor23 = pygame.image.load(os.path.join(os.path.dirname(__file__),'texture','23_floor.png')).convert_alpha()
        self.floor25 = pygame.image.load(os.path.join(os.path.dirname(__file__),'texture','25_floor.png')).convert_alpha()
        self.floor26 = pygame.image.load(os.path.join(os.path.dirname(__file__),'texture','26_floor.png')).convert_alpha()
        self.floor27 = pygame.image.load(os.path.join(os.path.dirname(__file__),'texture','27_floor.png')).convert_alpha()
        self.floor28 = pygame.image.load(os.path.join(os.path.dirname(__file__),'texture','28_floor.png')).convert_alpha()
        self.floor29 = pygame.image.load(os.path.join(os.path.dirname(__file__),'texture','29_floor.png')).convert_alpha()
        self.floor31 = pygame.image.load(os.path.join(os.path.dirname(__file__),'texture','31_floor.png')).convert_alpha()
        self.floor32 = pygame.image.load(os.path.join(os.path.dirname(__file__),'texture','32_floor.png')).convert_alpha()
        self.floor33 = pygame.image.load(os.path.join(os.path.dirname(__file__),'texture','33_floor.png')).convert_alpha()
        self.floor35 = pygame.image.load(os.path.join(os.path.dirname(__file__),'texture','35_floor.png')).convert_alpha()
        self.floor36 = pygame.image.load(os.path.join(os.path.dirname(__file__),'texture','36_floor.png')).convert_alpha()
        self.floor38 = pygame.image.load(os.path.join(os.path.dirname(__file__),'texture','38_floor.png')).convert_alpha()
        self.floor39 = pygame.image.load(os.path.join(os.path.dirname(__file__),'texture','39_floor.png')).convert_alpha()
        self.floor40 = pygame.image.load(os.path.join(os.path.dirname(__file__),'texture','40_floor.png')).convert_alpha()
        # If can optimize by for-loop is better. xD
        # can use dictionary to create for loop like in player.import_assets but cannot use the same variable name downward

        self.wall_lc = pygame.image.load(os.path.join(os.path.dirname(__file__),'texture','wall_lcorner.png')).convert_alpha()
        self.wall_rc = pygame.image.load(os.path.join(os.path.dirname(__file__),'texture','wall_rcorner.png')).convert_alpha()
        self.wall_lvt = pygame.image.load(os.path.join(os.path.dirname(__file__),'texture','wall_lvtail.png')).convert_alpha()
        self.wall_rvt = pygame.image.load(os.path.join(os.path.dirname(__file__),'texture','wall_rvtail.png')).convert_alpha()
        self.wall_h = pygame.image.load(os.path.join(os.path.dirname(__file__),'texture','wall_h.png')).convert_alpha()
        self.wall_lv = pygame.image.load(os.path.join(os.path.dirname(__file__),'texture','wall_lv.png')).convert_alpha()
        self.wall_rv = pygame.image.load(os.path.join(os.path.dirname(__file__),'texture','wall_rv.png')).convert_alpha()
        self.floor = pygame.image.load(os.path.join(os.path.dirname(__file__),'texture','floor.png')).convert_alpha()
        self.door = pygame.image.load(os.path.join(os.path.dirname(__file__),'texture','door.png')).convert_alpha()

        self.maze_wall = pygame.image.load(os.path.join(os.path.dirname(__file__),'texture','maze_wall.png')).convert_alpha()
        self.maze_wall_v = pygame.image.load(os.path.join(os.path.dirname(__file__),'texture','maze_wall_v.png')).convert_alpha()
        self.maze_wall_h = pygame.image.load(os.path.join(os.path.dirname(__file__),'texture','maze_wall_h.png')).convert_alpha()
        self.maze_wall_d = pygame.image.load(os.path.join(os.path.dirname(__file__),'texture','maze_wall_d.png')).convert_alpha()
        self.maze_floor = pygame.image.load(os.path.join(os.path.dirname(__file__),'texture','maze_floor.png')).convert_alpha()
        self.maze_floor_h = pygame.image.load(os.path.join(os.path.dirname(__file__),'texture','maze_floor_h.png')).convert_alpha()
        self.maze_floor_v = pygame.image.load(os.path.join(os.path.dirname(__file__),'texture','maze_floor_v.png')).convert_alpha()
        self.maze_floor_d = pygame.image.load(os.path.join(os.path.dirname(__file__),'texture','maze_floor_d.png')).convert_alpha()

        self.input_img = pygame.image.load(os.path.join(os.path.dirname(__file__),'texture','input.png')).convert_alpha()
        self.npc = pygame.image.load(os.path.join(os.path.dirname(__file__),'texture','npc.png')).convert_alpha()



    def create_edges(self):
        self.edge_left = pygame.draw.line(self.off_screen,(0,0,0,0),(0,-50),(0,850),width=1)
        self.edge_left = self.edge_left.move(-50,0)
        self.edge_right = pygame.draw.line(self.off_screen,(0,0,0,0),(1050,-50),(1050,850),width=1)
        self.edge_up = pygame.draw.line(self.off_screen,(0,0,0,0),(-50,0),(1050,0),width=1)
        self.edge_up = self.edge_up.move(0,-50)
        self.edge_down = pygame.draw.line(self.off_screen,(0,0,0,0),(-50,850),(1050,850),width=1)

    def get_mouse_pos(self):
        self.mouse_pos = pygame.mouse.get_pos()

    def setup(self):
        self.player = Player(self.spawn,self.all_sprites)
        self.maze = Maze(25,21)
        self.quiz = QuickMathGame()

    def refresh_game(self):
        self.map_index = 1
        self.prev_index = 1
        self.player.refresh_pos()
        self.player.refresh_stat()
        self.player.clear(-1)

    def run(self,dt):
        self.debug()
        self.import_menu_assets()
        self.get_mouse_pos()
        self.screen.fill('Black')
        self.screen.blit(self.off_screen,(-200,-200))
        self.load_menu(self.menu_index)
        if not self.map_index == 0:
            self.load_map(self.map_index, dt)
            self.all_sprites.custom_draw() # Draws the player
            self.all_sprites.update(dt) # Draws the player
            self.load_ingame_menu()
            self.check_edge()
            self.check_worldedge_collision(dt)
            if self.player.quiz_clear is False:
                self.fog()
            self.check_door()
            if self.showmsg:
                self.load_msg(self.currenttext)
            print(self.player.pos)

    def check_worldedge_collision(self,dt): # this can actually reuse in maze
        if self.world_edge:
            self.player.pos -= ((self.player.direction) * self.player.speed * dt)
            self.player.rect.center = self.player.pos
            self.world_edge = False
            #print('checked world edge')

    def check_edge(self):
        if self.player.rect.colliderect(self.edge_left):
            self.switch_map(self.edge_left_index)
        elif self.player.rect.colliderect(self.edge_right):
            self.switch_map(self.edge_right_index)
        elif self.player.rect.colliderect(self.edge_up):
            self.switch_map(self.edge_up_index)
        elif self.player.rect.colliderect(self.edge_down):
            self.switch_map(self.edge_down_index)

    def check_door(self):
        if self.player.rect.collidepoint(self.mouse_pos) and (pygame.mouse.get_pressed()[0]):
            try:
                if self.player.rect.colliderect(self.door_rect):
                    self.switch_map(self.door_index)
            except:
                pass
            
    def fog(self):
        keys = pygame.key.get_pressed()
        self.dimfog = pygame.Surface((1000,800))
        self.dimfog.set_alpha(self.fog_alpha)
        self.dimfog.fill('Grey')
        if self.map_index == 3 and self.player.pos.x <= 255:
            self.fog_alpha = 255 - self.player.pos.x
        if self.map_index == 8 and self.player.pos.y >= 545:
            self.fog_alpha = -545 + self.player.pos.y
        if self.map_index == 7 and (self.player.pos.x <= 255 and self.player.pos.y >= 545):
            if (255 - self.player.pos.x) > (-545 + self.player.pos.y):
                self.fog_alpha = -545 + self.player.pos.y
            else:
                self.fog_alpha = 255 - self.player.pos.x
        if self.map_index == 4:
            self.currenttext = "You lost inside the fog..."
            self.showmsg = True
            if self.prev_index == 3:
                self.map_index = 3
                self.player.pos.x = 800
                self.fog_alpha = 0
            elif self.prev_index == 8:
                self.map_index = 8
                self.player.pos.y = 200
                self.fog_alpha = 0
        self.screen.blit(self.dimfog,(0,0))
        if keys[pygame.K_SPACE]:
            self.showmsg = False

    def switch_map(self, index):
        if index == -1:
            self.world_edge = True
            #print('World Edge')
        else:
            self.prev_index = self.map_index
            self.map_index = index
            #print('map switched!')
            if self.prev_index - self.map_index == 1: # to right
                self.player.pos.x = 25
            elif self.prev_index - self.map_index == -1: # to left
                self.player.pos.x = 975
            elif self.prev_index - self.map_index == 4: # to Down
                self.player.pos.y = 25
            elif self.prev_index - self.map_index == -4: # to Up
                self.player.pos.y = 775

    def debug(self):
        pass

    def import_menu_assets(self):
        self.menu_font = pygame.font.Font(None, 80)

        self.gmenu_font = pygame.font.Font(None, 50)
        self.gmenu_back_surf = self.gmenu_font.render('Menu',True,'White')
        self.gmenu_back_rect = self.gmenu_back_surf.get_rect(center=(80,60))
        self.gmenu_block = pygame.Surface((120,60))
        self.gmenu_block.fill('Black')
        self.gmenu_block_rect = self.gmenu_block.get_rect(center=(80,60))
        self.gpopup_block = pygame.Surface((400,200))
        self.gpopup_block_rect = self.gpopup_block.get_rect(center=(750,650))
        self.gpopup_block.fill('Black')
        self.gmsg_block = pygame.Surface((500,300))
        self.gmsg_block.fill('Black')
        self.gmsg_block_rect = self.gmsg_block.get_rect(center=(500,400))

        self.menu_title = self.menu_font.render('Math World Adventure',True,'Cyan')
        self.menu_title_rect = self.menu_title.get_rect(center=(500,200))
        self.menu_cont = self.menu_font.render('Continue Game',True,'White')
        self.menu_cont_rect = self.menu_title.get_rect(center=(585,400))
        self.menu_start = self.menu_font.render('Start New Game',True,'White')
        self.menu_start_rect = self.menu_start.get_rect(center=(500,500))
        self.menu_exit_surf = self.menu_font.render('Exit Game',True,'White')
        self.menu_exit_rect = self.menu_exit_surf.get_rect(center=(500,600))

        self.pause_start = self.menu_font.render('Continue',True,'White')
        self.pause_start_rect = self.pause_start.get_rect(center=(500,400))
        self.pause_back = self.menu_font.render('Back to Main Menu',True,'White')
        self.pause_back_rect = self.pause_back.get_rect(bottomright=(950,750))

    def load_menu(self, index):
        if self.map_index == 0:
            if index == 0:  # Main Menu
                self.screen.blit(self.menu_title,self.menu_title_rect)
                self.screen.blit(self.menu_cont,self.menu_cont_rect)
                self.screen.blit(self.menu_start,self.menu_start_rect)
                self.screen.blit(self.menu_exit_surf,self.menu_exit_rect)

                if self.menu_cont_rect.collidepoint(self.mouse_pos) and (pygame.mouse.get_pressed()[0]):
                    self.map_index = self.prev_index
                if self.menu_exit_rect.collidepoint(self.mouse_pos) and (pygame.mouse.get_pressed()[0]):
                    pygame.quit()
                    exit()
                if self.menu_start_rect.collidepoint(self.mouse_pos) and (pygame.mouse.get_pressed()[0]):
                    self.refresh_game()
                    # Below should all be written as def NewGame for new game initialise
            elif index == 3: # Pause Menu
                    self.screen.blit(self.pause_start,self.pause_start_rect)
                    self.screen.blit(self.pause_back,self.pause_back_rect)
                    self.screen.blit(self.menu_exit_surf,self.menu_exit_rect)
                    if self.pause_start_rect.collidepoint(self.mouse_pos) and (pygame.mouse.get_pressed()[0]):
                        self.map_index = self.prev_index
                    if self.pause_back_rect.collidepoint(self.mouse_pos) and (pygame.mouse.get_pressed()[0]):
                        self.menu_index = 0
                    if self.menu_exit_rect.collidepoint(self.mouse_pos) and (pygame.mouse.get_pressed()[0]):
                        pygame.quit()
                        exit()

    def load_popup(self, name, greet, index): # Pop up box for interaction
        keys = pygame.key.get_pressed()
        if not self.map_index == 0: # Ensures in-game
            self.load_popuptext(name, greet, index)
            if self.gpopup_block_rect.collidepoint(self.mouse_pos):
                self.gpopup_block.set_alpha(255)
                self.popup_name.set_alpha(255)
                self.popuptext.set_alpha(255)
                self.popup_greet.set_alpha(255)
            else:
                self.gpopup_block.set_alpha(120)
                self.popup_name.set_alpha(120)
                self.popuptext.set_alpha(120)
                self.popup_greet.set_alpha(120)
            if self.popuptext_rect.collidepoint(self.mouse_pos):
                self.popup_color = pygame.Color(0,255,255)
                if (pygame.mouse.get_pressed()[0]):
                    if index == 1: # 1 refers to NPC
                        self.showmsg = True
                    elif index == 2: # 2 refers to doors
                        self.showmsg = False
                        self.map_index = self.door_index
                        self.tp(self.tpi[0],self.tpi[1])
                    elif index == 3: # Quiz Boss
                        self.showmsg = True
                    elif index == 4: # Final Boss
                        self.showmsg = True
                    else:
                        pass # add interact after clicked the buttons
                
            else:
                self.popup_color = pygame.Color(255,255,255)
            if keys[pygame.K_SPACE]:
                self.showmsg = False
                if index == 3:
                    self.map_index = self.door_index
                    self.tp(self.tpi[0],self.tpi[1])
                    self.timer = True
                elif index == 4:
                    self.map_index = 0
                    self.refresh_game()
            self.screen.blit(self.gpopup_block,self.gpopup_block_rect)
            self.screen.blit(self.popup_name,self.popup_name_rect)
            self.screen.blit(self.popup_greet,self.popup_greet_rect)
            self.screen.blit(self.popuptext,self.popuptext_rect)

    def tp(self, x, y):
        self.player.pos.x = x
        self.player.pos.y = y

    def load_msg(self, text):
        self.screen.blit(self.gmsg_block,self.gmsg_block_rect)
        self.gmsg_text = self.gmenu_font.render(text, True, 'White')
        self.gmsg_text_rect = self.gmsg_text.get_rect(topleft=(260,260))
        gexit_font = pygame.font.Font(None, 30)
        self.gmsg_exit = gexit_font.render("Press SPACE to exit", True, 'White')
        self.gmsg_exit_rect = self.gmsg_text.get_rect(topleft=(500,500))
        self.screen.blit(self.gmsg_text,self.gmsg_text_rect)
        self.screen.blit(self.gmsg_exit,self.gmsg_exit_rect)
        
            

    def load_popuptext(self, name, greet, index): # Text should input greetings (from npc class in player.py)
        self.popup_name = self.gmenu_font.render(name, True, 'White')
        self.popup_greet = self.gmenu_font.render(greet, True, 'White')
        if index == 1: # 1 refers to NPC, then have "Talk"
            self.popuptext = self.gmenu_font.render("Talk", True, self.popup_color)
        if index == 2: # 2 refers to doors, then have "Open"
            self.popuptext = self.gmenu_font.render("Go", True, self.popup_color)
        if index == 3: # 3 refers to Road / Cave, then have "Go"
            self.popuptext = self.gmenu_font.render("Go", True, self.popup_color)
        if index == 4: # 4 refers to Hostile, then have "Fight!"
            self.popuptext = self.gmenu_font.render("Fight!", True, self.popup_color)
        self.popup_name_rect = self.popup_name.get_rect(topleft=(560,570))
        self.popup_greet_rect = self.popup_greet.get_rect(topleft=(560,610))
        self.popuptext_rect = self.popuptext.get_rect(topleft=(850,700))
        
        
    
    def load_ingame_menu(self): # Menu for pausing
        if not self.map_index == 0: # Ensures in-game
            # Below build the in-game pause game menu (unopened)
            if self.gmenu_block_rect.collidepoint(self.mouse_pos):
                self.gmenu_back_surf.set_alpha(255)
                self.gmenu_block.set_alpha(255)
                if (pygame.mouse.get_pressed()[0]):
                    self.menu_index = 3
                    self.prev_index = self.map_index
                    self.map_index = 0
            else:
                self.gmenu_block.set_alpha(120)
                self.gmenu_back_surf.set_alpha(120)
            self.screen.blit(self.gmenu_block,self.gmenu_block_rect)
            self.screen.blit(self.gmenu_back_surf,self.gmenu_back_rect)

    def load_maze(self): 
        maze = self.maze.generate_maze()
        #print(maze)
        return maze

    def load_input_box(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RETURN]:
            try:
                self.answer = int(self.input_text)
                self.input_text = ''
                pygame.time.delay(100)
            except:
                self.input_text = ''
        elif keys[pygame.K_BACKSPACE]:
            self.input_text = self.input_text[:-1]
            pygame.time.delay(100)
        else:
            if keys[pygame.K_0]:
                self.input_text += '0'
                pygame.time.delay(120)
            elif keys[pygame.K_1]:
                self.input_text += '1'
                pygame.time.delay(120)
            elif keys[pygame.K_2]:
                self.input_text += '2'
                pygame.time.delay(120)
            elif keys[pygame.K_3]:
                self.input_text += '3'
                pygame.time.delay(120)
            elif keys[pygame.K_4]:
                self.input_text += '4'
                pygame.time.delay(120)
            elif keys[pygame.K_5]:
                self.input_text += '5'
                pygame.time.delay(120)
            elif keys[pygame.K_6]:
                self.input_text += '6'
                pygame.time.delay(120)
            elif keys[pygame.K_7]:
                self.input_text += '7'
                pygame.time.delay(120)
            elif keys[pygame.K_8]:
                self.input_text += '8'
                pygame.time.delay(120)
            elif keys[pygame.K_9]:
                self.input_text += '9'
                pygame.time.delay(120)
        self.input_rect = self.input_img.get_rect(topleft=(500,250))
        self.screen.blit(self.input_img,self.input_rect)
        txt_surface = self.menu_font.render(self.input_text, True, 'White')
        self.screen.blit(txt_surface, (600,375))
        

    def load_map(self, index, dt):
        if index == 0: # Should open menu (any)
            pass

        if index == 20: # Maze game interface

            # Below build the maze
            if self.maze_refresh:
                self.active_maze = self.load_maze()
                self.wall_points = []
                self.load_wall_point = True
            self.maze_refresh = False
            tx = 28 # topleft x
            ty = 6 # topleft y
            for y in range(len(self.active_maze)):
                tx = 28
                if y % 2 == 0:
                    for x in range(len(self.active_maze[y])):
                        if x % 2 == 0:
                            if self.active_maze[y][x] == 'WALL':
                                self.screen.blit(self.maze_wall_d,(tx,ty))
                                #wallrect = self.maze_wall_d.get_rect(topleft=(tx,ty))
                                #self.wall_rects.append((wallrect))
                            elif self.active_maze[y][x] == 'PATH':
                                self.screen.blit(self.maze_floor_d,(tx,ty))
                            tx += 8
                        elif x % 2 == 1:
                            if self.active_maze[y][x] == 'WALL':
                                self.screen.blit(self.maze_wall_h,(tx,ty))
                                #wallrect = self.maze_wall_d.get_rect(topleft=(tx,ty))
                                #self.wall_rects.append((wallrect))
                            elif self.active_maze[y][x] == 'PATH':
                                self.screen.blit(self.maze_floor_h,(tx,ty))
                            tx += 70
                    ty += 8
                if y % 2 == 1:
                    for x in range(len(self.active_maze[y])):
                        if x % 2 == 0:
                            if self.active_maze[y][x] == 'WALL':
                                self.screen.blit(self.maze_wall_v,(tx,ty))
                                #wallrect = self.maze_wall_d.get_rect(topleft=(tx,ty))
                                #self.wall_rects.append((wallrect))
                            elif self.active_maze[y][x] == 'PATH':
                                self.screen.blit(self.maze_floor_v,(tx,ty))
                            tx += 8
                        elif x % 2 == 1:
                            if self.active_maze[y][x] == 'WALL':
                                self.screen.blit(self.maze_wall,(tx,ty))
                                #wallrect = self.maze_wall_d.get_rect(topleft=(tx,ty))
                                #self.wall_rects.append((wallrect))
                            elif self.active_maze[y][x] == 'PATH':
                                self.screen.blit(self.maze_floor,(tx,ty))
                            tx += 70
                    ty += 70
            touched = False
            if self.load_wall_point:
                for pixel_x in range(1000):
                    for pixel_y in range(800):
                        if self.screen.get_at((pixel_x,pixel_y)) == (237,28,36,255):
                            self.wall_points.append((pixel_x,pixel_y))
                            self.load_wall_point = False

            for ind in range(len(self.wall_points)):
                if self.player.rect.collidepoint(self.wall_points[ind]):
                    touched = True
            if touched:
                print(touched, self.player.pos)
                self.player.pos -= ((self.player.direction) * self.player.speed * dt)
            print(len(self.wall_points),self.load_wall_point, self.player.pos, self.mouse_pos)

            # Below build the door (exit)
            self.door_rect = self.door.get_rect(center=(935,755))
            self.screen.blit(self.door,self.door_rect)
            self.door_index = 27

            if self.door_rect.colliderect(self.player):
                self.load_popup("Go Back?", "The maze will change.", 2)
                self.tpi = [500,400]

            # Below build the npc (reward)
            self.npc_1_rect = self.npc.get_rect(center=(70,50))
            self.screen.blit(self.door,self.npc_1_rect)

            if self.npc_1_rect.colliderect(self.player):
                self.load_popup("The Key", "You've found it.", 3)
                self.tpi = [500,400]
                self.currenttext = "Congratulations!"
                self.player.clear(1)

        if index == 24: # Quiz game interface
            quiztitle = self.gmenu_font.render("Finish 20 questions as fast as possible!", True, 'White')
            quiztitle2 = self.gmenu_font.render("Press Enter to Submit Answers.", True, 'White')
            quiztitle3 = self.gmenu_font.render("Opening Menu will NOT pause the game!", True, 'White')
            self.screen.blit(quiztitle,(200,50))
            self.screen.blit(quiztitle2,(200,100))
            self.screen.blit(quiztitle3,(200,150))

            if self.refresh_quiz:
                self.quiz.RefreshQuestion()
            self.refresh_quiz = False
            if self.timer:
                self.start_timer = time.time()
                self.timer = False
            #else:
                #start = time.time()
            if self.quiz.score < 20:
                self.ques_surf = self.menu_font.render(self.quiz.quesString, True, 'White')
                self.ques_surf_rect = self.ques_surf.get_rect(center=(500,300))
                self.screen.blit(self.ques_surf,self.ques_surf_rect)
                self.quiz_fbtext = ''
                #print(self.quiz.quesString)
                #self.quiz.input = int(input("Please input your answer: "))
                self.load_input_box()
                if self.answer == self.quiz.sol:
                    self.quiz_fbtext = "Score: " + str(self.quiz.score) + " Time Used: " + str(round(time.time() - self.start_timer,3))
                    self.refresh_quiz = True
                    self.quiz.score += 1
                else:
                    self.quiz_fbtext = "Score: " + str(self.quiz.score) + " Time Used: " + str(round(time.time() - self.start_timer,3))
                self.quiz_fb = self.menu_font.render(self.quiz_fbtext, True, 'White')
                self.screen.blit(self.quiz_fb,(100,600))
            if self.quiz.score == 20:
                end = time.time()
                length = end - self.start_timer
                self.timer = True
                self.quiz_result = f"You did it! Your time is: " + str(round(length,3)) + "s"
                self.map_index = 22

            self.door_rect = self.door.get_rect(center=(500,550))
            self.screen.blit(self.door,self.door_rect)
            self.door_index = 33
            if self.door_rect.colliderect(self.player):
                self.load_popup("Quit?", "Progress won't save.", 2)
                self.tpi = [500,400]
            
        if index == 22: # Quiz result interface
            keys = pygame.key.get_pressed()

            self.quiz_fb = self.menu_font.render(self.quiz_result, True, 'White')
            self.screen.blit(self.quiz_fb,(100,200))
            gexit_font = pygame.font.Font(None, 30)
            self.gmsg_exit = gexit_font.render("Press SPACE to exit", True, 'White')
            self.gmsg_exit_rect = self.gmsg_exit.get_rect(topleft=(500,500))
            self.screen.blit(self.gmsg_exit,self.gmsg_exit_rect)
            self.player.clear(0)
            if keys[pygame.K_SPACE]:
                self.switch_map(33)
                self.quiz_highscore = self.quiz.score
                self.quiz.score = 0
                self.refresh_quiz = True

        if index == 1:
            # Below build the floor
            self.screen.blit(self.floor1,(0,0))
            # Below build the edge
            self.edge_left_index = 2
            self.edge_right_index = -1
            self.edge_up_index = 5
            self.edge_down_index = -1
            # Below build the NPC
            self.npc_1_rect = self.npc.get_rect(center=(600,400))
            self.screen.blit(self.npc,self.npc_1_rect)
            if self.npc_1_rect.colliderect(self.player):
                self.load_popup("Guide", "Hi, I'm Guide.", 1)
                self.currenttext = "Go to quiz tower."
                if self.player.quiz_clear and not self.player.maze_clear:
                    self.currenttext = "Go to maze village."
                elif self.player.maze_clear:
                    self.currenttext = "Go to boss castle."

        if index == 2:
            # Below build the floor
            self.screen.blit(self.floor2,(0,0))
            # Below build the edge
            self.edge_left_index = 3
            self.edge_right_index = 1
            self.edge_up_index = 6
            self.edge_down_index = -1

        if index == 3:
            # Below build the floor
            self.screen.blit(self.floor3,(0,0))
            # Below build the edge
            self.edge_left_index = 4
            self.edge_right_index = 2
            self.edge_up_index = 7
            self.edge_down_index = -1
            # Below build the NPC
            self.npc_1_rect = self.npc.get_rect(center=(700,600))
            self.screen.blit(self.npc,self.npc_1_rect)
            if self.npc_1_rect.colliderect(self.player):
                self.load_popup("Guide", "Hi, I'm Guide.", 1)
                self.currenttext = "Go to quiz tower."
                if self.player.quiz_clear and not self.player.maze_clear:
                    self.currenttext = "Go to maze village."
                elif self.player.maze_clear:
                    self.currenttext = "Go to boss castle."

        if index == 4:
            # Below build the floor
            self.screen.blit(self.floor4,(0,0))
            # Below build the edge
            self.edge_left_index = -1
            self.edge_right_index = 3
            self.edge_up_index = 8
            self.edge_down_index = -1
            # Below build the NPC
            self.npc_2_rect = self.npc.get_rect(center=(600,400))
            self.screen.blit(self.npc,self.npc_2_rect)
            if self.npc_2_rect.colliderect(self.player):
                self.load_popup("Maze NPC", "Hi, I'm Maze NPC.", 1)
                self.currenttext = "Maze is under the ground."
            # Below build the door
            self.door_rect = self.door.get_rect(center=(500,700))
            self.screen.blit(self.door,self.door_rect)
            self.door_index = 19

            if self.door_rect.colliderect(self.player):
                self.load_popup("Maze Underground", "Enter?", 2)
                self.tpi = [500,400]

        if index == 5:
            # Below build the floor
            self.screen.blit(self.floor5,(0,0))
            # Below build the edge
            self.edge_left_index = 6
            self.edge_right_index = -1
            self.edge_up_index = 9
            self.edge_down_index = 1

        if index == 6:
            # Below build the floor
            self.screen.blit(self.floor6,(0,0))
            # Below build the edge
            self.edge_left_index = 7
            self.edge_right_index = 5
            self.edge_up_index = 10
            self.edge_down_index = 2

        if index == 7:
            # Below build the floor
            self.screen.blit(self.floor7,(0,0))
            # Below build the edge
            self.edge_left_index = 8
            self.edge_right_index = 6
            self.edge_up_index = 11
            self.edge_down_index = 3
        
        if index == 8:
            # Below build the floor
            self.screen.blit(self.floor8,(0,0))
            # Below build the edge
            self.edge_left_index = -1
            self.edge_right_index = 7
            self.edge_up_index = 12
            self.edge_down_index = 4
            # Below build the NPC
            self.npc_1_rect = self.npc.get_rect(center=(100,300))
            self.screen.blit(self.npc,self.npc_1_rect)
            if self.npc_1_rect.colliderect(self.player):
                self.load_popup("Guide", "Hi, I'm Guide.", 1)
                self.currenttext = "Go to quiz tower."
                if self.player.quiz_clear and not self.player.maze_clear:
                    self.currenttext = "Go to maze village."
                elif self.player.maze_clear:
                    self.currenttext = "Go to boss castle."

        if index == 9:
            # Below build the floor
            self.screen.blit(self.floor9,(0,0))
            # Below build the edge
            self.edge_left_index = 10
            self.edge_right_index = -1
            self.edge_up_index = 13
            self.edge_down_index = 5

        if index == 10:
            # Below build the floor
            self.screen.blit(self.floor10,(0,0))
            # Below build the edge
            self.edge_left_index = 11
            self.edge_right_index = 9
            self.edge_up_index = 14
            self.edge_down_index = 6

        if index == 11:
            # Below build the floor
            self.screen.blit(self.floor11,(0,0))
            # Below build the edge
            self.edge_left_index = 12
            self.edge_right_index = 10
            self.edge_up_index = 15
            self.edge_down_index = 7

        if index == 12:
            # Below build the floor
            self.screen.blit(self.floor12,(0,0))
            # Below build the edge
            self.edge_left_index = -1
            self.edge_right_index = 11
            self.edge_up_index = 16
            self.edge_down_index = 8

        if index == 13:
            # Below build the floor
            self.screen.blit(self.floor13,(0,0))

            # Below build the door
            self.door_rect = self.door.get_rect(center=(527,527))
            self.screen.blit(self.door,self.door_rect)
            self.door_index = 17

            if self.door_rect.colliderect(self.player):
                self.load_popup("Quiz Tower", "Enter?", 2)
                self.tpi = [500,600]

            # Below build the edge
            self.edge_left_index = 14
            self.edge_right_index = -1
            self.edge_up_index = -1
            self.edge_down_index = 9

        if index == 14:
            # Below build the floor
            self.screen.blit(self.floor14,(0,0))
            # Below build the edge
            self.edge_left_index = 15
            self.edge_right_index = 13
            self.edge_up_index = -1
            self.edge_down_index = 10

        if index == 15:
            # Below build the floor
            self.screen.blit(self.floor15,(0,0))
            # Below build the edge
            self.edge_left_index = 16
            self.edge_right_index = 14
            self.edge_up_index = -1
            self.edge_down_index = 11

        if index == 16:
            # Below build the floor
            self.screen.blit(self.floor16,(0,0))
            # Below build the door
            self.door_rect = self.door.get_rect(center=(477,175))
            self.screen.blit(self.door,self.door_rect)
            self.door_index = 32

            if self.door_rect.colliderect(self.player):
                if self.player.maze_clear:
                    self.load_popup("Boss Castle", "Enter?", 2)
                    self.tpi = [500,600]
                else:
                    self.load_popup("Boss Castle", "Not yet unlocked.", 1)
                    self.currenttext = "Get the key at maze village."

            # Below build the edge
            self.edge_left_index = -1
            self.edge_right_index = 15
            self.edge_up_index = -1
            self.edge_down_index = 12

        if index == 17:
            # Below build the floor
            self.screen.blit(self.floor17,(0,0))

            # Below build the door
            self.door_rect = self.door.get_rect(center=(500,700))
            self.screen.blit(self.door,self.door_rect)
            self.door_index = 13

            if self.door_rect.colliderect(self.player):
                self.load_popup("Leave Quiz Tower", "Go Back?", 2)
                self.tpi = [525,600]

            # Below build the edge
            self.edge_left_index = -1
            self.edge_right_index = -1
            self.edge_up_index = 21
            self.edge_down_index = -1

        if index == 19:
            # Below build the floor
            self.screen.blit(self.floor19,(0,0))
            # Below build the door
            self.door_rect = self.door.get_rect(center=(200,400))
            self.screen.blit(self.door,self.door_rect)
            self.door_index = 4

            if self.door_rect.colliderect(self.player):
                self.load_popup("Leave underground.", "Go Back?", 2)
                self.tpi = [500,500]
            
            # Below build the NPC
            self.npc_1_rect = self.npc.get_rect(center=(600,400))
            self.screen.blit(self.npc,self.npc_1_rect)
            if self.npc_1_rect.colliderect(self.player):
                self.load_popup("Maze NPC", "Hi, I'm Maze NPC.", 1)
                self.currenttext = "Welcome to maze village."

            # Below build the edge
            self.edge_left_index = -1
            self.edge_right_index = -1
            self.edge_up_index = 23
            self.edge_down_index = -1

        if index == 23:
            # Below build the floor
            self.screen.blit(self.floor23,(0,0))
            # Below build the edge
            self.edge_left_index = -1
            self.edge_right_index = -1
            self.edge_up_index = 27
            self.edge_down_index = 19

        if index == 27:
            # Below build the floor
            self.screen.blit(self.floor27,(0,0))
            # Below build the edge
            self.edge_left_index = -1
            self.edge_right_index = -1
            self.edge_up_index = -1
            self.edge_down_index = 23
            # Below build the door
            self.door_rect = self.door.get_rect(center=(500,200))
            self.screen.blit(self.npc,self.door_rect) # This is an NPC looking door
            self.door_index = 20

            if self.door_rect.colliderect(self.player):
                self.load_popup("Maze Boss", "Enter the maze?.", 3)
                self.tpi = [925,755]
                self.currenttext = "Entering the Maze..."
                self.maze_refresh = True
            # Below build the npc
            self.npc_2_rect = self.npc.get_rect(center=(600,400))
            self.screen.blit(self.npc,self.npc_2_rect)
            if self.npc_2_rect.colliderect(self.player):
                self.load_popup("Guide", "Hi, I'm Guide.", 1)
                if self.player.maze_clear:
                    self.currenttext = "Go fight the boss!"
                else:
                    self.currenttext = "Go clear the maze!"
            

        if index == 21:
            self.screen.blit(self.floor21,(0,0))
            # Below build the edge
            self.edge_left_index = -1
            self.edge_right_index = -1
            self.edge_up_index = 25
            self.edge_down_index = 17

        if index == 25:
            # Below build the floor
            self.screen.blit(self.floor25,(0,0))
            # Below build the edge
            self.edge_left_index = -1
            self.edge_right_index = -1
            self.edge_up_index = 29
            self.edge_down_index = 21

        if index == 29:
            # Below build the floor
            self.screen.blit(self.floor29,(0,0))
            # Below build the edge
            self.edge_left_index = -1
            self.edge_right_index = -1
            self.edge_up_index = 33
            self.edge_down_index = 25

            # Below build the door
            self.door_rect = self.door.get_rect(center=(300,400))
            self.screen.blit(self.npc,self.door_rect) # This is an NPC looking door
            self.door_index = 3

            if self.door_rect.colliderect(self.player):
                if self.player.quiz_clear:
                    self.load_popup("Helper", "Go to maze village?", 3)
                    self.tpi = [500,400]
                    self.currenttext = "I will help you!"
                else:
                    self.load_popup("Helper", "Go to maze village?", 1)
                    self.currenttext = "Go clear the quiz first!"

        if index == 33:
            # Below build the floor
            self.screen.blit(self.floor33,(0,0))
            # Below build the door
            self.door_rect = self.door.get_rect(center=(500,200))
            self.screen.blit(self.npc,self.door_rect) # This is an NPC looking door
            self.door_index = 24

            if self.door_rect.colliderect(self.player):
                self.load_popup("Quiz Boss", "Start the quiz?", 3)
                self.tpi = [500,400]
                self.currenttext = "Prepare for challenge!"

            # Below build the NPC
            self.npc_1_rect = self.npc.get_rect(center=(600,400))
            self.screen.blit(self.npc,self.npc_1_rect)
            if self.npc_1_rect.colliderect(self.player):
                self.load_popup("Guide", "Hi, I'm Guide.", 1)
                self.currenttext = "Go clear the quiz!"
                if self.player.quiz_clear:
                    self.currenttext = "Go down one floor."
            
            # Below build the edge
            self.edge_left_index = -1
            self.edge_right_index = -1
            self.edge_up_index = -1
            self.edge_down_index = 29

        if index == 32:
            # Below build the floor
            self.screen.blit(self.floor32,(0,0))
            # Below build the door
            self.door_rect = self.door.get_rect(center=(500,700))
            self.screen.blit(self.door,self.door_rect)
            self.door_index = 16

            if self.door_rect.colliderect(self.player):
                self.load_popup("Leave Boss Castle", "Go Back?", 2)
                self.tpi = [500,300]
            
            # Below build the edge
            self.edge_left_index = -1
            self.edge_right_index = -1
            self.edge_up_index = 36
            self.edge_down_index = -1

        if index == 36:
            # Below build the floor
            self.screen.blit(self.floor36,(0,0))
            # Below build the edge
            self.edge_left_index = -1
            self.edge_right_index = -1
            self.edge_up_index = 40
            self.edge_down_index = 32

        if index == 40:
            # Below build the floor
            self.screen.blit(self.floor40,(0,0))
            # Below build the edge
            self.edge_left_index = -1
            self.edge_right_index = -1
            self.edge_up_index = -1
            self.edge_down_index = 36
            # Below build the NPC
            self.door_rect = self.door.get_rect(center=(450,300))
            self.screen.blit(self.npc,self.door_rect) # This is an NPC looking door
            self.door_index = 24

            if self.door_rect.colliderect(self.player):
                self.load_popup("Boss", "Hi, I'm Boss.", 4)
                self.currenttext = "You saved the world!"

            
            

class PlayerGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.screen = pygame.display.get_surface()

    def custom_draw(self):
        for sprite in self.sprites():
            self.screen.blit(sprite.image, sprite.rect)

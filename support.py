from os import walk
import os
import pygame

def import_folder(path):
    surface_list = []

    for folder_name, sub_folder, imgs in walk(path):
        for img in imgs:
            #print(imgs)
            full_path = os.path.join(folder_name,img)
            image_surf = pygame.image.load(full_path).convert_alpha()
            #print(full_path)
            surface_list.append(image_surf)
    return surface_list
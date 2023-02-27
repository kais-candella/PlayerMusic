import tkinter as tk
import os
import pygame
from pygame import mixer


player = tk.Tk()

screen_height = 400
screen_width = 500 



pygame.mixer.init()

image = pygame.image.load("tyler.jpg")

# cherche la musique et la jouer
music_file_path = "SWEET.mp3"

if os.path.exists(music_file_path):
    pygame.mixer.music.load(music_file_path)
    pygame.mixer.music.play(-1)
    
else:
    print("Error: music file not found")

# definie une fonction pause et unpause pour la musique 
def pause_music():
    pygame.mixer.music.pause(start_img)

def unpause_music():
    pygame.mixer.music.unpause()




pygame.init()
player = pygame.display.set_mode((screen_height, screen_width))
pygame.display.set_caption('Button Demo')

#ajout image 
start_img = pygame.image.load('Bouton_jouer.png').convert_alpha()
start_img = pygame.transform.scale(start_img, (int(start_img.get_width() * 0.1), int(start_img.get_height() * 0.1))) # redimensionner l'image

suivant_img = pygame.image.load('forward_button.png').convert_alpha()
suivant_img = pygame.transform.scale(suivant_img, (int(suivant_img.get_width() * 0.1), int(suivant_img.get_height() * 0.1))) # redimensionner l'image

rewind_img = pygame.image.load('rewind_button.png').convert_alpha()
rewind_img = pygame.transform.scale(rewind_img, (int(rewind_img.get_width() * 0.1), int(rewind_img.get_height() * 0.1))) # redimensionner l'image

#image fond
fond_img = pygame.image.load('carré_noir.png').convert_alpha()
fond_img = pygame.transform.scale(fond_img, (int(fond_img.get_width() * 0.5), int(fond_img.get_height() * 0.5))) # redimensionner l'image

#Buton
class Button():
    def __init__(self,x ,y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (175,400)

    def draw(self):
        #dessin du bouton
        player.blit(self.image, (self.rect.x, self.rect.y))

    def is_clicked(self, pos):
        #renvoie True si le bouton est cliqué
        return self.rect.collidepoint(pos)

#Buton
class Button2():
    def __init__(self,x ,y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (265,400)

    def draw(self):
        #dessin du bouton
        player.blit(self.image, (self.rect.x, self.rect.y))

    def is_clicked(self, pos):
        #renvoie True si le bouton est cliqué
        return self.rect.collidepoint(pos)

#Buton
class Button3():
    def __init__(self,x ,y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (85,400)

    def draw(self):
        #dessin du bouton
        player.blit(self.image, (self.rect.x, self.rect.y))

    def is_clicked(self, pos):
        #renvoie True si le bouton est cliqué
        return self.rect.collidepoint(pos)


#arriere de la musique
class Button4():
    def __init__(self,x ,y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (73,50)

    def draw(self):
        #dessin du bouton
        player.blit(self.image, (self.rect.x, self.rect.y))


        
#buton parametre 
start_button = Button(100 ,200 ,start_img)
suivant_button = Button2(100 ,200 ,suivant_img)
rewind_button = Button3(100 ,200 ,rewind_img)
fond_button = Button4(100 ,200 ,fond_img)



#game loop
run = True
while run:

    player.fill(('#443C68'))

    start_button.draw()
    suivant_button.draw()
    rewind_button.draw()
    fond_button.draw()
    
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False

        pygame.display.update()


pygame.quit()

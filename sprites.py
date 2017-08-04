import pygame

#surfaces to hold the sprite images
babydragon = pygame.image.load("babydragon.png")
bug = pygame.image.load("bug.png")
elderdragon = pygame.image.load("elderdragon.png")
grapeape = pygame.image.load("grapeape.png")
madelephant = pygame.image.load("madelephant.png")
mantis = pygame.image.load("mantis.png")
phoenix = pygame.image.load("phoenix.png")
razorbear = pygame.image.load("razorbear.png")
tadpol = pygame.image.load("tadpol.png")
vixen = pygame.image.load("vixen.png")
smileycyclops = pygame.image.load("smileycyclops.png")

#lists that contain the sprites
enemy_list1 = [grapeape,bug]
enemy_list2 = [mantis,vixen]
enemy_list3 = [babydragon,tadpol]
enemy_list4 = [razorbear,smileycyclops]
enemy_list5 = [phoenix,madelephant]
enemy_boss = [elderdragon]